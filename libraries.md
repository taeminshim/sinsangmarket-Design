# 화면 기준

## 라이브러리

| 플랫폼 | 구분 | 라이브러리 이름 | 원본 파일 | libraryKey |
|---|---|---|---|---|
| 모바일 | 디자인 시스템 | [신상마켓] M_Design system Guide | [열기](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6) | `lk-9a385b22b4c0ce859159f0dd15e7dd52d0fcebba58a24a90ee76ab5cdb6957d7a6bd9e1193fd1b828d62c97f60769c8740d0445a26a4e7ea5391172d3d3ede47` |
| 모바일 | UI Builder | M_UI Builder | [열기](https://www.figma.com/design/7eHgyABjNbCL1fVzpbZ1IX) | `lk-9ff569ad6cebb0c5f0dd35fb8b44fca75f5e91bd90f42b9af2f63bb1498acf8384b8150d423af1daa10f23d147ca59b3966705eb8a5ca745ed4c1e117d784372` |
| PC | 디자인 시스템 | [신상마켓] PC_Design system Guide | [열기](https://www.figma.com/design/hzFtDckwBKxfz3QQBrOnHa) | `lk-fd4e5f0647c7ecbdeb2f2e5d463df19402a8c01a95c0edd0f85a98a097a3d9a87c67887543555a217b404c7dce0fe1d4862f640f9446837964a293d6e8e5025d` |
| PC | UI Builder | PC UI Builder | [열기](https://www.figma.com/design/aFam9mIsTVZqNmKdHHYq0f) | `lk-e98052a784de80869dbfd36e80ae628d31c5cbe901838008f59c24e242e0097993d79398e78a31053247900e95c786c9fdbc7e31e6ac132507eca1a913c84017` |

> 조직에는 신상애드, 글로벌 로고 대응 등 **다른 라이브러리도 많아요.** 컴포넌트를 검색할 때는 반드시 위 4개 라이브러리로 범위를 좁혀요.

디자인 시스템 = 토큰·기본 컴포넌트 (Typography, Grid, Colors, Indentations 4px, Iconography, Shadows, Corner radius, Navigation, Buttons, UI Elements, Forms, Filter Tab).
UI Builder = 디자인 시스템을 조합한 화면 단위 블록과 템플릿.

## 모바일 (iOS 기준)

| 항목 | 기준 |
|---|---|
| 화면 폭 | **375** (iOS 템플릿 프레임 375×812) |
| 좌우 마진 | 16 → 콘텐츠 343 |
| 그리드 | 4컬럼, 거터 8, Fluid |
| 간격 단위 | 4px (Indentations) |
| 화면 구성 | 상단바(디자인 시스템 `★top Bar`) → 콘텐츠 → 하단탭(`❤︎bottomTab`·`❤︎bottom Bar`). 빌더 `B-Top_screen`·`B-Navigation`은 필요할 때만 |

- AOS(360) 템플릿도 빌더에 있지만 팀 기준상 **AOS 화면은 따로 치지 않아요.**
- 섹션 간 여백(라인 없을 때 / Divider 있을 때 / 광고+리스트 / 검색·필터·타이틀 조합 등)은 빌더의 [간격 가이드](https://www.figma.com/design/7eHgyABjNbCL1fVzpbZ1IX?node-id=480-34034)를 따라요. 주로 8 · 12 · 16 · 20 · 24 단위를 써요.
- 출처: M_Design system Guide › Grid, M_UI Builder › Building on templates

## PC (1440 기준)

| 항목 | 기준 |
|---|---|
| 기준 해상도 | **1440** |
| 추가 대응 | 1200 · 2000 — **꼭 필요한 화면만** |
| 콘텐츠 프레임 | 1200 (좌우 32 → 콘텐츠 1136) — 빌더 템플릿 기준, 1200·1440 공용 |
| 2000 | 별도 템플릿·컴포넌트 사이즈 사용 (`_2000px` 계열) |
| 페이지 구조 | GNB → (Breadcrumb) → 지면 → FNB |

**기본 여백** (빌더 [간격 가이드](https://www.figma.com/design/aFam9mIsTVZqNmKdHHYq0f?node-id=198-44524) 기준)

| 위치 | 여백 |
|---|---|
| GNB 아래 → 지면 시작 | 48 (상단에 필터가 붙는 지면은 32) |
| Breadcrumb 아래 → 지면 시작 | 24 (1200·1440) / 32 (2000) |
| 지면 끝 → FNB | 100 |

- 상품 정보·오버레이·쇼케이스 컴포넌트는 `Size = 1200px | 1440px | 2000px` variant로 해상도를 맞춰요. 해상도별로 새로 그리지 말고 variant만 바꿔요.
- Tab 하단 여백, 카테고리 Tab 하단 여백, 영문 지면은 간격 가이드에서 확인해요.

## 공통

- 상품 이미지는 3:4 원본, 1:1 썸네일은 3:4의 센터 크롭이에요. 빌더의 `Thumbnail/Standard 3:4`, `Thumbnail/Standard 1:1`을 써요.
- 썸네일 상태는 `State` variant로 표현해요: Default / Empty / inactive / soldout.
