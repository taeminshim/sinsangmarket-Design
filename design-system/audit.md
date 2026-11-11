# 그린 뒤 검수 (디자인 시스템 린트)

화면을 다 그리면 Claude가 아래 스크립트를 Figma에서 실행해서 규칙 위반을 찾고, 걸린 항목을 고친 뒤 결과를 보고해요.
스크립트는 **읽기만** 하고 화면을 바꾸지 않아요. 사람이 직접 점검할 때도 같은 기준을 써요.

## 검사 항목

| 코드 | 검사 | 걸리는 경우 | 고치는 법 |
|---|---|---|---|
| `FILL` | 하드코딩 색 | 색 스타일이 연결되지 않은 채움 | [foundations](foundations.md)의 색 스타일 연결 |
| `STROKE` | 하드코딩 선 | 색 스타일이 연결되지 않은 선 | `Line/…` 스타일 연결 |
| `TEXT` | 하드코딩 글자 | 텍스트 스타일이 연결되지 않은 텍스트 | `sh2sb18` 같은 텍스트 스타일 연결 |
| `DETACHED` | 해제된 시스템 컴포넌트 | 이름이 `btn…`, `chip…`, `tag…`, `textLink…` 등인데 인스턴스가 아닌 프레임 | 디자인 시스템 컴포넌트로 다시 넣기 |
| `LOCAL` | 라이브러리 밖 컴포넌트 | 이 파일에서 직접 만든 컴포넌트의 인스턴스 | 라이브러리 컴포넌트로 교체, 또는 `❤︎` 커스텀이면 이름 표기 확인 |
| `FRAME` | 화면 규격 | 최상위 화면 폭이 375(iOS)·1440·1200·2000(PC)이 아님 | 규격에 맞게 조정 |
| `LIBRARY` | 다른 라이브러리 | 쓰인 컴포넌트 목록 중 신상마켓 4개 라이브러리에 없는 것 | 아래 "라이브러리 확인" 단계에서 판별 |

> 빌더 골격 블록(`B-`)을 해제한 것은 허용이라 `DETACHED`로 잡지 않아요.
> 인스턴스 안쪽(컴포넌트가 원래 가진 색·글자)은 검사하지 않아요. 우리가 직접 만든 레이어만 봐요.
> 라이브러리 원본 파일(디자인 시스템·빌더) 안에서 실행하면 모든 컴포넌트가 `LOCAL`로 잡혀요. 작업 파일에서 실행해요.

## 실행 방법 (Claude용)

1. 검사할 화면 프레임 ID를 `FRAME_ID`에 넣어 `use_figma`로 실행한다 (읽기 전용).
2. 결과의 `issues`를 코드별로 고친다. 의도한 예외(예: 이미지 위 그라데이션 딤)는 보고에 사유를 적는다.
3. **라이브러리 확인:** 결과의 `components` 목록에서 이름을 `search_design_system`(`includeLibraryKeys` = 해당 플랫폼 디자인 시스템 + 빌더)으로 찾는다. 같은 키가 나오지 않는 컴포넌트는 다른 라이브러리 것이므로 교체한다. PC에서 `Buttons/…`, `bt_…`처럼 이름 규칙에 안 맞는 컴포넌트는 PC 디자인 시스템 테스트 페이지 것이므로 교체한다.
4. 고친 뒤 한 번 더 실행해서 `issues`가 비었는지(또는 사유가 있는 예외만 남았는지) 확인한다.

```js
// 신상마켓 디자인 시스템 검수 — 읽기 전용
const FRAME_ID = 'FRAME_ID';
const root = await figma.getNodeByIdAsync(FRAME_ID);
if (!root) throw new Error('frame not found: ' + FRAME_ID);
let pg = root; while (pg && pg.type !== 'PAGE') pg = pg.parent;
if (pg) await figma.setCurrentPageAsync(pg);

const DS_NAME = /^(♥︎|❤︎|★)?(btn|chip|chips|tag|textLink|imgChip|searchInput|subSearchInput|searchBar|textArea|textInput|checkBox|checkbox|checkCircle|checkLine|radioButton|switch|dropdown|tabBar)/;
const issues = [];
const components = new Map();
const add = (code, n, note) => issues.push({ code, id: n.id, name: n.name, note });

const solidUnstyled = (paints, styleId) =>
  styleId === '' && Array.isArray(paints) && paints.some(p => p.visible !== false && p.type === 'SOLID');

async function walk(n) {
  if (n.type === 'INSTANCE') {
    const mc = await n.getMainComponentAsync();
    if (mc) {
      const owner = mc.parent && mc.parent.type === 'COMPONENT_SET' ? mc.parent : mc;
      const key = owner.key;
      if (!components.has(key)) components.set(key, { name: owner.name, key, remote: mc.remote, count: 0 });
      components.get(key).count++;
      if (!mc.remote) add('LOCAL', n, owner.name);
    }
    return; // 인스턴스 내부는 검사하지 않음
  }
  if (n.type === 'TEXT') {
    if (n.textStyleId === '' || n.textStyleId === figma.mixed) add('TEXT', n, n.characters.slice(0, 20));
    if (typeof n.fillStyleId === 'string' && solidUnstyled(n.fills, n.fillStyleId)) add('FILL', n, 'text color');
    return;
  }
  if ('fills' in n && typeof n.fillStyleId === 'string' && solidUnstyled(n.fills, n.fillStyleId)) add('FILL', n, '');
  if ('strokes' in n && typeof n.strokeStyleId === 'string' && solidUnstyled(n.strokes, n.strokeStyleId)) add('STROKE', n, '');
  if (n.type === 'FRAME' && DS_NAME.test(n.name)) add('DETACHED', n, 'system component name on a plain frame');
  if ('children' in n) for (const c of n.children) await walk(c);
}

const w = Math.round(root.width);
if (![375, 1440, 1200, 2000].includes(w)) add('FRAME', root, 'width ' + w);
if ('children' in root) for (const c of root.children) await walk(c);

const count = {};
for (const i of issues) count[i.code] = (count[i.code] || 0) + 1;
return {
  frame: root.name, width: w, summary: count,
  issues: issues.slice(0, 80), truncated: issues.length > 80,
  components: [...components.values()].sort((a, b) => b.count - a.count)
};
```

## 보고 형식

```
검수 결과: (화면 이름)
- 고친 것: FILL 3건 → 색 스타일 연결, TEXT 2건 → 텍스트 스타일 연결
- 남긴 예외: FILL 1건 (이미지 위 그라데이션 딤 — 스타일 없음)
- 라이브러리 확인: 사용 컴포넌트 12종 모두 신상마켓 라이브러리
```
