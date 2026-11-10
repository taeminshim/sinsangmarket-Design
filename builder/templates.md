# 빌더 템플릿 — 배치·여백 참고

화면은 디자인 시스템에서 시작해요. 템플릿은 **화면 유형별로 무엇을 어떤 순서·간격으로 쌓는지 참고**하는 자료예요. 신규 화면에서 배치가 막막할 때 가장 가까운 유형을 열어 보고, 필요하면 템플릿 프레임을 그대로 가져와 써도 돼요.

## 모바일 — M_UI Builder › [Building on templates](https://www.figma.com/design/7eHgyABjNbCL1fVzpbZ1IX?node-id=169-12991)

| 템플릿 | 언제 | 크기 | key |
|---|---|---|---|
| `IOS-1depth Frame` | 하단 탭이 있는 1depth 지면 (홈, 카테고리, 매장 등) | 375×812 | `c50e711c88df35b97bd390553241df4a1fa03866` |
| `IOS-2depth Frame` | 뒤로가기가 있는 하위 화면 | 375×812 | `0d6dd1af04e3e8e97118076ab4b631b5ce35582d` |
| `IOS-1depth List` | 1depth 상품 리스트 지면 | 375×1678 | `5d4c1561ed8979e253d6a99c2e02965f7a4a3666` |
| `IOS-2depth List` | 하위 상품 리스트 지면 | 375×1678 | `fc009cc2bbd0e30124ddded9199beb5de389d747` |
| `IOS-info` | 정보 확인 화면 | 375×1809 | `a2d20a57c4181c6d462dc896f5b05b3b3335ec8a` |
| `IOS-form` | 입력 폼 화면 | 375×1351 | `79e3176c30c6f3e7355cd8ff40a7017f5e48f1cf` |

AOS 템플릿(`AOS-info`, `AOS-form`)도 있지만 팀 기준상 쓰지 않아요.

같은 페이지에 `padding`(세트, Property 1=Default·last, 텍스트 속성 1개, key `3ae4cadc03a3dc39803ae075a1022fc6cdd9b55c`)도 게시돼 있어요. 템플릿 안에서 여백 값을 표시하는 라벨로 보여요 — 화면 결과물에 넣는 요소인지는 빌더 담당자 확인이 필요해요.

**화면 유형별 블록 조합** — [간격 가이드](https://www.figma.com/design/7eHgyABjNbCL1fVzpbZ1IX?node-id=480-34034)에 실제 예시가 있어요.

| 유형 | 예시 |
|---|---|
| 홈탭 | 기본 탭 / 기본 탭+카테고리 / 섹션별 여백(라인 없음) / 섹션별 여백(Divider) |
| 카테고리 | 섹션별 여백(광고+리스트) / 카테고리 1depth / 2depth |
| 검색 | 검색 전 / 검색 중 / 검색결과(상품) / 검색결과(매장) |
| 섹션 | 섹션+리스트(검색+필터+타이틀) / 섹션+리스트(타이틀+카테고리탭+check) |
| 리스트 타입별 | Fixed tab |
| 목록/입력 | 목록 / 입력 |

## PC — PC UI Builder › [Building on templates](https://www.figma.com/design/aFam9mIsTVZqNmKdHHYq0f?node-id=3-84)

| 화면 구조 | 예시 지면 |
|---|---|
| GNB + Breadcrumb + 지면 + FNB | 상품 리스트 지면 (전체신상 등) |
| GNB + SNB + Table + FNB | 마이페이지 (주문 내역 등) |
| 필터 있는 지면 | 좌측 필터 + 상품 그리드 (우리매장 찜리스트 등) |

| 템플릿 컴포넌트 | 크기 | key |
|---|---|---|
| `B-지면(전체신상)_2000px` | 2000 | `40fc63406a9df9e361d5477a2f243fc842f40550` |
| `B-마이페이지_1440px` | 1200 프레임 | `1466ef908c7f678d10fc015a19aadc07d877898a` |
| `B-마이페이지_2000px` | 2000 | `2841921f53a49a5db532bc3576404d5e0cc4a9d3` |
| `B-우리매장찜리스트` | 2000 | `76e38a4c221f24f6da634c9f8fa4f355c9507103` |

여백은 [PC 간격 가이드](https://www.figma.com/design/aFam9mIsTVZqNmKdHHYq0f?node-id=198-44524)를 따라요: 기본 여백 / 하단 필터 노출 / Breadcrumb 노출 지면(1200·1440, 2000) / Tab 하단 / 카테고리 Tab 하단 / 영문 지면.
