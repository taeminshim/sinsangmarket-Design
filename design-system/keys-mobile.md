# 모바일 자주 쓰는 키 모음

화면을 그릴 때 **매번 검색하지 않고 바로 불러오기 위한 표**예요. 필요한 항목만 찾아서 쓰면 돼요.
빌더(M_UI Builder) 컴포넌트 키는 [builder/mobile](../builder/mobile.md)에 있어요.

> **키가 안 먹으면 검색 결과를 따라요.** 라이브러리가 업데이트되면 키가 바뀔 수 있어요. 표에 없는 컴포넌트는 `includeLibraryKeys`로 범위를 좁혀 검색해요.
> 2026-11-02 기준, 모바일 디자인 시스템(M_Design system Guide)에서 확인한 값이에요. PC는 [builder/pc](../builder/pc.md)와 PC 라이브러리에서 따로 확인해요.

불러오는 법
- 세트(`component_set`)는 `figma.importComponentSetByKeyAsync(key)`, 단일 컴포넌트는 `importComponentByKeyAsync(key)`
- 스타일은 `figma.importStyleByKeyAsync(key)` 후 `setFillStyleIdAsync` / `setTextStyleIdAsync`로 연결

## 컴포넌트 — 세트

| 이름 | 용도 | 주요 속성 | key |
|---|---|---|---|
| `btnFilledSemiMedium01` | 핑크 채움 버튼 (높이 40) | State, Show Icon | `9f14320f12442d3ba2c8e17a982621eae82f6b16` |
| `btnFilledSemiMedium02` | 그라데이션 채움 | 〃 | `0ce87c39f143ce333f73fca0657a67d34415ce2d` |
| `btnFilledSemiMedium03` | 반투명 어두운 채움 | 〃 | `7110604f94c07940c03392b9d87db5a7391affdf` |
| `btnFilledSemiMedium04` | 블루 채움 | 〃 | `26b9710959d2338e9183084a16735cea998759c3` |
| `btnFilledSemiMedium05` | 멤버십 그라데이션 채움 | 〃 | `026a2f6773d0ff98902389c328c42af486bf776c` |
| `btnFilledSemiMedium06` | 검정 채움 | 〃 | `49c9e66688ca15f3a329d192abcb36036232890d` |
| `btnOutlineSemiMedium01` | 아웃라인 01 | State, Show Icon | `370a6de4d9a146d32da29e731967ee9927d814ca` |
| `btnOutlineSemiMedium02` | 아웃라인 02 | 〃 | `1d46d17a69159917cfac1c3202875ddfe30123ce` |
| `btnOutlineSemiMedium03` | 아웃라인 03 | 〃 | `24d45e3cf4744acfee42e68b0ff380f62d5a23eb` |
| `btnOutlineSemiMedium04` | 아웃라인 04 | 〃 | `5a5e7c65dd175108cffc82ddf8b28e63a0ac558c` |
| `btnOutlineSemiMedium05` | 아웃라인 05 | 〃 | `0010a44dfa05fece93c8344655dcc5f6b9f8b2d8` |
| `btnOutlineSemiMedium06` | 검정 아웃라인 | 〃 | `bd7c4e1212e9c2de461df429a2d84231f1566b50` |
| `chipOutlineSmall01` | 필터 칩 (높이 32) | Show Icon(None·Both·Left·Right·Only), State(Default·Selected·Disabled) | `a69133ec852c8aad7fba158e0d44cf75cc32c578` |
| `❤︎status Bar` | iOS 상태바 | color=White BG·Black BG | `b4a232e3a9c03426e8bf0598d49d027be11490e2` |
| `❤︎top Bar` | 상단바 (375×48) | Type, Logo, Navigatio icon, Title, Action btn | `aa9242d608ac3ebeeb92e33e8fedd90e21a24f86` |
| `★top Bar` | 상단바 (등록 대기) | type, logo, Navigation icon, Title | `ea3426d4b667e6b20be7671c054e94154ff65595` |
| `searchInput01` | 라인형 검색 입력 | status | `9a4e0015e5e6c1b3e327c6ade68a1cb928b51f77` |
| `searchInput02` | 채움형 검색 입력 | status | `05c6a1db40734fd6f770f716a7499dab9a4a23e3` |
| `popUp` | 중앙 팝업 | — | `c36272758d67cc043ca8396f799c47775b49523a` |

버튼 컬러 번호 의미는 [components](components.md)의 "버튼 컬러 번호"를 봐요. 위 표는 **SemiMedium(40)** 만 정리했고, 다른 사이즈는 `btn{Style}{Size}{NN}` 이름으로 검색해요.

## 컴포넌트 — 단일

| 이름 | 용도 | key |
|---|---|---|
| `ic_arrow_open` | 아래 화살표(드롭다운 열기) | `4cb9646a441081022b1d962304536dfd205fce0b` |
| `ic_filter` | 필터 아이콘 | `4b3d0781c41c0ca7e6fa63f2fddc46e375812e2e` |
| `modal` | 모달 | `f902446c8ddf014892ff6f3904c00df179e5891e` |

## 색 스타일 (Paint)

| 스타일 | 값 | key |
|---|---|---|
| `Primary/primary01` | #FB4760 | `43b6522a1802f60ddc02f1aeff7f7bae16bb8ff1` |
| `Primary/primary03` | #FEECEF | `d940cdb1a3253f1ec6ac762e22af63b7f719ca19` |
| `Primary/primary04` | #FFFFFF | `c9448d7f6dc65fb285b73a15e6804c531865cb3c` |
| `Primary/primary05` | #000000 | `0fd3f67eb3f4f3e0da2afde8e572f6c2df756a72` |
| `Text/g100` | #222222 | `f69f1233f93cafa65ebff387512cd80480ea86a5` |
| `Text/g80` | #686E7B | `03ffe90efe6da5c4ecc5ab7ecdc7a6654d1d0795` |
| `Text/g70` | #8F97A7 | `52af8342001d635d04365116a9bc5d066f1ccb7f` |
| `Text/g60` | #A6ADBD | `7699f1dc7058f7880414de792e59f0da6d384515` |
| `Text/g50` | #BEC5D2 | `97455cb8d23d2ec9921c11435809dd6b1ae9ae8f` |
| `BG/g05` | #F6F6F7 | `959a76941a2f4a3ff9333bed3d94e601b63dcec8` |
| `BG/g10` | #F5F6FB | `f62aca6e4d3899bdb7f398d802fe5cb86ad82899` |
| `Line/g10` | 연한 구분선 | `b1bc21ade7d988d2172157162654f1573b8763d1` |
| `Line/g20` | 입력 테두리 | `ced0449d526e97baadb65cdd19dbef9144059b3f` |
| `Line/g30` | #DFE3ED | `94b9048c579b1a954e31f6d051728e8a87744c8e` |

## 텍스트 스타일

| 스타일 | 크기(행간) | key |
|---|---|---|
| `h2sb24` | 24(32) | `fbf7c6399f48c79f7a46ecaadd554499fb91f50e` |
| `sh1sb20` | 20(28) | `28d8e795c9dd5bdddf99e3330d2b7ca2c41d88f5` |
| `sh2sb18` | 18(26) | `bbd425bb0497c30437d2e66d6d1063a31a09eeff` |
| `sh3sb16` | 16(22) | `a3bc9decae249b042306a1bc48a0d3b408bec459` |
| `b2sb14` | 14(20) | `8667831b898658d305cb1c1e7d31cbc8e2bc1134` |
| `b2r14` | 14(20) | `277cfd201fc5c21b8d25274d09054604cfa12d95` |
| `b3sb13` | 13(18) | `3ed9c93ac30e8b8bc97fffea166fc6e1042782b4` |
| `b3r13` | 13(18) | `c44a28a1677d59a85a600cfbf848724f2c47b5d0` |
| `b4sb12` | 12(16) | `0e3252e78b1d28eca86953791c7583ae1b6266e0` |
| `b4r12` | 12(16) | `5892cbe61ee192378ff28a5fd28b9638dd194051` |

텍스트를 바꾸거나 스타일을 연결하기 전에 해당 폰트를 먼저 불러와요.

## 쓸 때 주의 (실제 작업에서 겪은 것)

| 상황 | 주의 |
|---|---|
| 버튼 글자 바꾸기 | 글자 속성 이름이 `Text#…` 형태라서, `componentProperties` 키 중 `Text#`로 시작하는 것을 찾아 `setProperties`로 바꿔요 |
| 칩 아이콘 바꾸기 | 칩 안에는 아이콘이 중첩돼 있어요. **바깥 아이콘만** `swapComponent`하고 그 안쪽 아이콘은 건드리지 않아요 (건드리면 오류가 나고, 오류가 나면 그 호출의 수정이 전부 취소돼요) |
| 칩을 줄일 때 | 지우지 말고 `visible = false`로 숨기면 레이아웃이 알아서 당겨져요 |
| 오버레이 썸네일 (`Thumbnail/Overlay 3:4`) | 폭이 210보다 작으면 안쪽 `Info/Overlay`의 `Size`를 `Meduim (209이하)`로 바꿔요. 이미지는 썸네일 자체의 채움이에요 |
| 색상 바꾸기 | 헤더 배경처럼 이미지가 채워진 프레임은 `setFillStyleIdAsync`로 스타일을 연결하면 이미지가 사라져요 |
