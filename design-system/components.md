# 디자인 시스템 컴포넌트 사용법

버튼·칩·태그·텍스트링크·입력 같은 기본 컴포넌트는 **이름만 보면 생김새를 알 수 있게** 지어져 있어요. 그래서 목록을 외우지 않고 이름 규칙으로 찾아 써요.
이 컴포넌트들은 **해제(Detach)하지 않아요.** 속성(variant)만 바꿔서 써요.

원본: [M_Design system Guide](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=0-1) · [PC_Design system Guide](https://www.figma.com/design/hzFtDckwBKxfz3QQBrOnHa?node-id=0-1)

## 이름 규칙

```
{종류}{스타일}{사이즈}{컬러번호}
btn  Filled  Large  01   →  btnFilledLarge01
```

| 종류 | 이름 형식 | 스타일 | 사이즈 | 컬러 번호 |
|---|---|---|---|---|
| 버튼 | `btn{Style}{Size}{NN}` | Filled · FilledRound · FilledTonal · FilledTonalRound · Outline · OutlineRound · OutlineBg · OutlineBgRound · Text · TextRound | Large 50 · Medium 46 · SemiMedium 40 · Small 32 | 01~06 (Text는 01~07, OutlineBg는 02 없음) |
| 텍스트 링크 | `textLink{Line?}{Size}{NN}` | Default · Line(밑줄) | Large 20 · Medium 20 · Small 18 | 01~07 |
| 칩 | `chip{Style}{Size}{NN}` | Filled · FilledSquare · FilledDepth · FilledImage(Depth) · Outline · OutlineSquare · OutlineImage | Large 46 · Medium 40 · Small 32 | 01~04 |
| 이미지 칩 | `imgChip{Size}01` | — | Large · Medium · Small | 01 |
| 태그 | `tag{Style}{Size}{NN}` | Filled · Outline · Text · Etc | Large 28 · Medium 26 · SemiMedium · Small 16 | 01~05 |
| 검색 입력 | 모바일 `searchInput{NN}` · `subSearchInput{NN}` / PC `searchBar{Size}{NN}` | — | PC: Large 46 · Small 32 | 01 라인형 · 02 채움형 |
| 텍스트 영역 | 모바일 `textArea{NN}` / PC `textAreaFlexible{NN}` · `textAreaFixed{NN}` | Flexible(내용 따라 늘어남) · Fixed(고정 높이 후 스크롤) | — | 01 기본 · 02 bg10 · 03 흰 배경 |

**공통 속성(variant)**
- `State`: Default · Hover&Pressed · Disabled · Loading(버튼) / Selected(칩)
- `Show Icon`: None · Left · Right · Both · Only
- 정렬 `Align`: Left · Center · Right (텍스트 링크)

### 버튼 컬러 번호 (Filled 기준)

| 번호 | 색 |
|---|---|
| 01 | Primary 핑크 |
| 02 | Primary 그라데이션 |
| 03 | 반투명 어두운 색 (이미지 위) |
| 04 | 블루 |
| 05 | 멤버십 그라데이션 (블루→라임) |
| 06 | 검정 |

다른 스타일(Tonal, Outline, Text)의 번호별 색은 [버튼 가이드](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=24469-54439)와 [PC 버튼 스타일(컬러)](https://www.figma.com/design/hzFtDckwBKxfz3QQBrOnHa?node-id=1605-29926)에서 확인해요. 같은 번호라도 스타일마다 색이 달라요.

### 커스텀 버튼

특정 화면 전용 버튼은 `btnCustom{Style}{Color}{사용영역}` 형식이에요. 예: `btnCustomLargePrimary01Order`(주문 하단 버튼), `btnCustomIconBG01ProductUpload`(상품 등록). 같은 영역을 만들 때만 써요.

## 종류별 위치와 규칙

| 종류 | 모바일 섹션 | PC 섹션 | 사용 규칙 |
|---|---|---|---|
| 버튼 | [M. Buttons](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=24469-54439) | [M. Buttons](https://www.figma.com/design/hzFtDckwBKxfz3QQBrOnHa?node-id=18085-50329) | 높이는 사이즈로만 조절. Small 32는 라운드 4, Large·Medium은 6 |
| 텍스트 링크 | [N. textLink](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=24469-54440) | [L. textLink](https://www.figma.com/design/hzFtDckwBKxfz3QQBrOnHa?node-id=18085-50330) | 더보기·이동 링크 |
| 칩 | [F. Chips](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=24459-46483) | [F. Chips](https://www.figma.com/design/hzFtDckwBKxfz3QQBrOnHa?node-id=17610-59058) | 필터·카테고리 선택. 선택은 `State=Selected` |
| 태그 | [G. Tag](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=30291-26552) | [G. Tag](https://www.figma.com/design/hzFtDckwBKxfz3QQBrOnHa?node-id=22957-27841) | 상태·속성 표시 (클릭 없음) |
| UI 요소 | [H. UI Elements](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=24469-20909) | [H. UI Element](https://www.figma.com/design/hzFtDckwBKxfz3QQBrOnHa?node-id=24953-30508) | 체크박스·체크서클·체크라인·라디오·스위치·슬라이더·툴팁·토스트·팝업·로딩·Divider |
| 탭 | [I. Tab Bar](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=24469-22982) | Tab (시스템 네비게이션) | `fixed tab`(너비 N등분) · `scrollable tab`(일정 간격) · `tabBarSegment01` · `tabBarSlider01~03` |
| 배지 | [J. Badge](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=24469-22991) | Badge/… | 순위·알림·이미지 업로드 표시 |
| 폼 | [K. Forms](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=27141-56082) | [I. Forms](https://www.figma.com/design/hzFtDckwBKxfz3QQBrOnHa?node-id=21172-59448) | 아래 "입력 규칙" |
| 설명 텍스트 | [L. Description](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=24469-53707) | [J. Description](https://www.figma.com/design/hzFtDckwBKxfz3QQBrOnHa?node-id=18077-49939) | `labeledTextBullet` · `Number` · `Icon` 01/02, notice, accordion |
| 바텀시트·모달 | [D. Bottom Sheet/Modal](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=32948-62048) | [D. Layer](https://www.figma.com/design/hzFtDckwBKxfz3QQBrOnHa?node-id=24803-58234) | 아래 "모달 규칙" |
| 에러 | [E. Error Case](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=24459-25233) | [E. Error Case](https://www.figma.com/design/hzFtDckwBKxfz3QQBrOnHa?node-id=17610-59057) | 데이터 없음·네트워크 오류 (`dataNotice`, `error Case`) |
| 시스템 바 | [C. iOS Bars](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=32958-54318) | GNB · SNB · FNB · Breadcrumb ([시스템 네비게이션](https://www.figma.com/design/hzFtDckwBKxfz3QQBrOnHa?node-id=18054-25898)) | 상단바·하단탭·플로팅·필터바 |
| 테이블 (PC) | — | [K. Table](https://www.figma.com/design/hzFtDckwBKxfz3QQBrOnHa?node-id=18054-25039) | 도매(`❤︎dome/…`) · 소매(`❤︎Some/…`) 테이블, 페이지네이션 |
| 아이콘 | [A. Icon](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=24434-31552) | [A. Icon](https://www.figma.com/design/hzFtDckwBKxfz3QQBrOnHa?node-id=17610-59052) | `ic_이름`(라인) · `filled/ic_이름_filled`(채움). 사이즈 16·18·20·24 |

## 입력 규칙 (Forms)

- 입력·드롭다운 테두리는 `Line/g20`으로 통일해요.
- 모바일 입력: 좌 16 / 우 16 (아이콘 있으면 12), 상하 13. 아이콘 영역 24×24, 아이콘 크기 16·18·20·24, 아이콘 두 개면 간격 8.
- PC 입력: 높이 46이면 좌 16 / 우 16(아이콘 있으면 12), 높이 32면 좌 12 / 우 12(아이콘 있으면 8).
- 드롭다운: 최소 높이 46, 두 줄까지 위 정렬로 대응하고 세 줄 이상은 말줄임. 아이콘 영역 20, 아이콘 16.
- 텍스트 영역: Flexible은 내용에 따라 늘어나고, Fixed는 정해진 높이에서 스크롤해요.
- 에러 상태 variant가 따로 있어요 (Error, Error Focus, Error Time Limit 등).

## 모달·바텀시트 규칙

**모바일 모달**
- 버튼: 1개, 또는 2개(가로·세로 배치) 사용 가능.
- 콘텐츠 자유형 여백: 상 4 / 하 12 / 좌우 16 (바텀시트와 같음).
- 최대 높이: 화면의 70%. 넘으면 콘텐츠 안에서 스크롤.
- 최소 너비: 최소 해상도 320 − 패딩 (패딩 20이면 280, 40이면 240). 패딩 20/40을 섞어 쓰지 않아요.
- 딤 영역 동작은 프로젝트마다 정의 (시스템에서 정하지 않음).

**PC 레이어 모달**
- 사이즈: Medium 520 · Small 360 · Small 320 · XSmall 320.
- 콘텐츠 영역 최대 높이 505. 넘으면 스크롤, 스크롤 끝에서 하단 패딩 24.
- 상단: 타이틀 + 닫기, 또는 타이틀 + 닫기 + 다른 액션 버튼.

## 찾아서 쓰는 순서

1. 필요한 요소의 **종류·스타일·사이즈·컬러**를 정해 이름을 만들어요. 예: 화면 하단 주요 버튼 → `btnFilledLarge01`
2. 모바일이면 M_Design system Guide, PC면 PC_Design system Guide에서 그 이름을 찾아요.
3. 인스턴스를 놓고 `State`, `Show Icon` 같은 속성만 바꿔요. 해제하지 않아요.
4. 상품·매장 썸네일과 카드는 빌더에서 가져와요. 그 밖에 맞는 게 없으면 빌더 골격 블록(`B-`)을 확인하고, 그래도 없으면 커스텀(`❤︎`)으로 만들어 팀에 공유해요.
