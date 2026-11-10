# 파운데이션 — 색·타이포·라운드·그림자·간격

신상마켓 디자인 시스템은 **변수(Variables)가 아니라 스타일(Styles)** 로 토큰을 관리해요. 색·텍스트·그림자는 모두 라이브러리 스타일을 연결해서 쓰고, 값을 직접 입력하지 않아요.
스타일 이름은 모바일(M)과 PC가 거의 같지만 **키는 라이브러리마다 달라요.** 모바일 화면엔 M_Design system Guide 스타일, PC 화면엔 PC_Design system Guide 스타일을 써요.

원본: [M Color](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=24434-19978) · [M Type Scale](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=24434-19973) · [M Radius](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=24434-19999) · [M Shadows](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=24434-20004) · [PC Color](https://www.figma.com/design/hzFtDckwBKxfz3QQBrOnHa?node-id=17610-59050) · [PC Type Scale](https://www.figma.com/design/hzFtDckwBKxfz3QQBrOnHa?node-id=17610-59049)

## 색 (Paint styles)

| 그룹 | 스타일 | 값 | 쓰임 |
|---|---|---|---|
| Primary | `Primary/primary01` | #FB4760 | 브랜드 메인 |
| | `Primary/primary02` | #EC2843 | 진한 메인 |
| | `Primary/primary03` | #FEECEF | 연한 메인 배경 |
| | `Primary/primary06` | #FFDCE2 | 연한 핑크 (2025-03 도매 멤버십 체험판용으로 추가) |
| | `Primary/primary07` | #C62558 | 더 진한 핑크 |
| | `Primary/primary08` | #FEF2F4 | 가장 연한 핑크 배경 |
| | `Primary/primary04` · `05` | #FFFFFF · #000000 | 흰색 · 검정 |
| | `Primary/gradient` | 그라데이션 | 브랜드 그라데이션 |
| Secondary | `Secondary/secondary01` · `02` · `03` | #4759FB · #2B3EE6 · #EAEFFF | 블루 계열 |
| | `Secondary/secondary04` · `05` · `06` | #FF7C44 · #FF6827 · #FFECDB | 오렌지 계열 |
| Text | `Text/g100` | #222222 | 기본 텍스트 |
| | `Text/g80` | #686E7B | 보조 텍스트 (서브텍스트는 g80으로 통일, V2.63) |
| | `Text/g70` · `g60` · `g50` | #8F97A7 · #A6ADBD · #BEC5D2 | 약한 텍스트 · placeholder · 비활성 |
| Line | `Line/g100` ~ `Line/g10` | #222222 ~ #F5F6FB | 구분선·테두리 (입력 필드 테두리는 g20) |
| BG | `BG/g100` ~ `BG/g05` | #222222 ~ #F6F6F7 | 배경 (g10 #F5F6FB, g05 #F6F6F7) |
| Service | `Service/error` | #FA1818 | 에러 |
| | `Service/warning` | #FFD600 (PC #F6A300) | 경고 |
| | `Service/links&Info` | #2B66FD | 링크·안내 |
| | `Service/success` | #1BDA17 (PC #0DAA19) | 성공 |
| Membership | `Mbs/mbs01` · `mbs02` | #1F5EFF · #E5FE1E | 신상 멤버십 |
| | `Mbs/gradient01` · `02` | 그라데이션 | 멤버십 배지·버튼 |
| Etc | `Etc/b70` ~ `Etc/b2` | 검정 70% ~ 2% | 딤·오버레이 |
| | `Etc/w90` ~ `Etc/w5` | 흰색 90% ~ 5% | 이미지 위 요소 |

> PC에는 `Secondary/Dealibird`(#00197D)가 추가로 있고, 일부 이름 표기가 달라요(`mbs/…` 소문자, `Service/link&info`). `Flowkit/…` 색은 플로우 문서용이라 화면에 쓰지 않아요.

## 타이포 (Text styles) — Pretendard

이름 규칙: **용도 + 굵기 + 사이즈** (카멜 표기). 예: `sh2sb18` = Subhead2 · SemiBold · 18px
Pretendard는 국내·글로벌용이고, 중국어 화면은 시스템 폰트에 같은 스타일 값을 적용해요 (스타일 설명 기준).
굵기 약어: `b` Bold · `sb` SemiBold · `m` Medium · `r` Regular

| 용도 | 모바일 스타일 | 크기(행간) | PC에 추가로 있는 것 |
|---|---|---|---|
| Heading | `h1sb32` · `h3sb28` · `h2sb24` | 32(40) · 28(36) · 24(32) | `h1m40` 40(50), `h2m38` 38(48), `h3sb32`, `h4b28`·`h4sb28`, `h5b24`·`h5sb24`·`h5m24`·`h5r24` |
| Subhead | `sh1sb20` · `sh1r20` | 20(28) | |
| | `sh2sb18` · `sh2r18` | 18(26) | `sh2m18`, `sh3r18` |
| | `sh3sb16` · `sh3r16` | 16(22) | `sh3m16` |
| Body | `b1sb15` · `b1r15` | 15(20) | `b1m15` |
| | `b2sb14` · `b2r14` | 14(20) | `b2m14` |
| | `b3sb13` · `b3r13` | 13(18) | `b3m13` |
| | `b4sb12` · `b4r12` | 12(16) | `b4b12`, `b4m12`, `b5r11` 11(16) |
| Caption | `c1sb10` · `c1r10` | 10(14) | |

팀 기준: 섹션 타이틀은 18px(`sh2sb18`), 썸네일 옆 타이틀은 16px(`sh3sb16`). 서브텍스트 색은 `Text/g80`으로 통일했어요.

## 라운드 (Corner radius)

| 값 | 이름 | 쓰는 곳 |
|---|---|---|
| 0 | none | 여러 컴포넌트 |
| 3 | XSmall | 체크박스 |
| 4 | Small | 버튼 Small 32 |
| 6 | Medium | 버튼 Large 50·Medium 46, 드롭다운, 입력, 스낵바, 썸네일, 툴팁 |
| 10 | Large | 팝업 |
| 20 | — | 바텀시트 |
| 100% | XLarge | Round 버튼, 인디케이터, 토글, 체크서클, 스위치 |

## 그림자 (Effect styles)

| 스타일 | 값 (x y blur · 검정 투명도) |
|---|---|
| `Shadow/Type_1` | 0 1 3 · 10% |
| `Shadow/Type_2` | 0 1 3 · 22% |
| `Shadow/Type_3` | 0 2 7 · 22% |
| `Shadow/Type_4` | 0 4 8 · 20% |
| `Shadow/Type_5` | 0 10 20 · 15% |
| `Shadow/Type_6` | 0 20 50 · 15% |
| `Shadow/Type_7` (모바일만) | -20 0 50 · 30% |

번호가 클수록 더 떠 있는 요소에 써요. 가이드에 정리된 역할 순서는 테이블·작은 카드·버튼·말풍선·입력 필드·리스트 → 모달·팝업 → 사이드 오버레이예요. 요소별 정확한 타입은 [Shadows 가이드](https://www.figma.com/design/5WsL9kg8fteVvSDUw4L1s6?node-id=24434-20004)에서 확인해요.
PC는 이름이 `Shadow/Type1` ~ `Type6` (밑줄 없음)이에요.

## 간격과 그리드

- 간격은 **4px 단위**(Indentations)로 써요.
- 모바일 그리드: Small 0–767 · 4컬럼 · 마진 16 · 거터 8 / Medium(태블릿) 768–1024 · 8컬럼 · 마진 24 · 거터 16.
- 화면별 여백은 [libraries](../libraries.md)를 봐요.

## 컴포넌트 표기 규칙 (디자인팀 룰)

| 표기 | 의미 |
|---|---|
| 표기 없음 | 디자인 시스템 컴포넌트 (개발과 합의 완료) |
| `★` 이름 앞 | 개발과 협의된 **시스템 등록 대기** 컴포넌트 |
| `❤︎` / `♥︎` 이름 앞 | **디자인팀 내부용** 커스텀 컴포넌트 |
| `B-` 이름 앞 | UI Builder 블록 (해제 가능) |

디자인 시스템 컴포넌트가 아닌 것은 모두 커스텀으로 분류해요.
