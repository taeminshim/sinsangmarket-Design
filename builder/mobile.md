# 모바일 빌더 — M_UI Builder

[M_UI Builder 열기](https://www.figma.com/design/7eHgyABjNbCL1fVzpbZ1IX)

화면은 **디자인 시스템에서 시작**해요. 빌더에서는 주로 **상품 썸네일·상품 카드·매장 썸네일**을 가져오고, 화면 골격 블록(`B-`)은 필요할 때만 써요.
key는 Figma에서 `importComponentByKeyAsync`(단일) / `importComponentSetByKeyAsync`(세트)로 불러올 때 써요.

## 상품 카드 (Product_Card)

| 컴포넌트 | 종류 | 언제 | 주요 속성 | key |
|---|---|---|---|---|
| `Standard_Card` | 단일 | 기본 상품 카드 (썸네일 + 정보) | Instance(swap), Show Thumbnail, Show btn | `11c85afb8a5300c1b979eb421c2d86c3b588d8a6` |
| `Thumbnail/Standard 3:4` | 세트 | 3:4 상품 썸네일 | State=Default·Empty_white·Empty_gray·inacitve·soldout, badge·checkbox·rank·zzim·tag | `b8748356f32ee25c231f0f8721c60b9ef78805cd` |
| `Thumbnail/Standard 1:1` | 세트 | 1:1 상품 썸네일 | State, badge·checkbox·rank·zzim | `5b0b744f6a368032f33d8c31a74efb527ae4f74e` |
| `Thumbnail/Overlay 3:4` | 세트 | 정보가 이미지 위에 얹히는 3:4 썸네일 | State, Ovelay_Info, badge·checkbox·rank·zzim | `dbb87cb77b17e21988854e1dc085dd0e60df22de` |
| `Thumbnail/Overlay 1:1` | 세트 | 오버레이 1:1 썸네일 | State, Ovelay_Info 등 | `937e24019610bbd2936448e0b5547f2a0b1f7ca2` |
| `Info/Text` | 세트 | 썸네일 아래 상품 정보 | Size=Large 2열·Small 3열, ActiveStatus, 가격·할인율·원가·타이틀·브랜드·랭크·찜수·AD 토글 | `806a14f13092f3e0e1d716a5a6edc02580b2eae5` |
| `Info/Overlay` | 세트 | 이미지 위 상품 정보 | Size=Large(210↑)·Meduim(209↓)·Small(160↓), ActiveStatus | `a31286bb63b34bfc5aa56b29d88e83b52cbfe6e6` |
| `badge` | 세트 | 썸네일 배지 | Thumb Size=2단 156↑·3단 96↑·3단 95↓, Show details, Show Video | `2c3c1ddee4bd9a9aca3f608b4c1ec8e5432e55cc` |
| `rank` | 세트 | 순위 변동 표시 | default·up·down·disable·new | `a15cd0868faa87f03ed4d724d429862e187b88b7` |
| `num` | 세트 | 순위 숫자 | area=left·right·area3 | `9ca4efc7c143d014a1bef1fb7031285f5d890c79` |
| `thumb_top/zzim` | 단일 | 썸네일 우상단 찜 | — | `7265a408349353e5c1559797cce6b06b94ef91e4` |
| `thumb_top/alarm` | 단일 | 썸네일 우상단 알림 | — | `a3ea4f1715f52fa155eacd0bc018e526af3f6fda` |
| `Showcase-Card` | 단일 | 가로형 상품 요약 카드 | — | `2d3558e2fd473e008b44e680fea8641aad025bac` |
| `Thumbnail-1:0.833` | 세트 | 가로가 더 긴 썸네일 (1:0.833) | State=Default·Empty_white·Empty_gray·inactive | `e41dfa6ac2d247c99477643a9832f8f79616eb22` |
| `Thumbnail-1:1.465` | 세트 | 세로로 긴 썸네일 (1:1.465) | State=Default·Empty_white·Empty_gray·inactive | `edb8e21e74564787185c4dd8e981b1fed2c166ef` |

## 매장 (Store_badge)

| 컴포넌트 | 종류 | 언제 | 주요 속성 | key |
|---|---|---|---|---|
| `Store_thumb` | 세트 | 매장 썸네일 + 멤버십 배지 | Thumnail=80·72·54·50·48·44·36·32, mbs_badge, thumb_img, thumb_empty | `83a1059d5559e99f4b3ad4d532a54cfd6a0718ab` |
| `Store_thumb_empty` ⚠️ 미게시 | 세트 | 매장 이미지 없을 때 | size=71↑·70↓, Color=gray·white | `9d8209d9ecde2cda588c848b2c7339489d444c53` |
| `mbs_badge` ⚠️ 미게시 | 세트 | 멤버십 배지 단독 | 노출=48↑·47↓ | `56172baa3611aee8569c07c88a07b982c081f597` |

> ⚠️ `Store_thumb_empty`, `mbs_badge`는 빌더 원본에는 있지만 **라이브러리에 게시되지 않아** 작업 파일에서 key로 불러오면 실패해요. 당분간 `Store_thumb`의 `thumb_empty`·`mbs_badge` 속성을 켜서 대신 써요.

## 목록 (Table)

| 컴포넌트 | 언제 | key |
|---|---|---|
| `Showcase_card_내상품` | 내 상품 한 줄 | `4f7f8535f25aa01bf08e0b1f136627634e1a71e3` |
| `Showcase_card/장바구니` | 장바구니 상품 한 줄 | `ee19da0f17a14716e02148057ec3bec76b5e6bdc` |
| `Showcase_card/주문목록내역` | 주문 내역 한 줄 (Title·Sub text·Price·Show option) | `a3238f55e6eec84d7974dcb2acc334a0b5dd4d4f` |
| `Container/COM/내상품_list` | 내 상품 목록 묶음 | `5da695247cfe535ee003d4388dc7d53f64a833bc` |
| `Container/COM/매장주문(cart)_list` | 매장주문 장바구니 목록 | `f262ca94dc6ccacb1320f546afbdd9f13953a23f` |
| `Container/COM/신상배송(cart)_list` | 신상배송 장바구니 목록 | `59d1fb03e430cb89a58bdac159b1c93da67f09dc` |
| `Container/COM/주문목록내역` | 주문 내역 목록 묶음 | `03812f67bf8d83cbf1769440f50330b6bf2416a0` |

## 팝업 (Custom UI)

| 컴포넌트 | 언제 | key |
|---|---|---|
| `Custom>Popup` | 중앙 팝업 (체크박스 문구 옵션) | `411c8af5f5785a1d0e0c08f64a1209b304fae710` |
| `Custom>Alert(textlink)` | 텍스트 링크가 있는 알림 | `ef96b12e6cd8308d5df7771c67079c10a43335e3` |

## 화면 골격 블록 — 필요할 때만 (Navigations)

디자인 시스템에 마땅한 게 없거나 빌더 블록 조합이 더 빠를 때 써요. `B-` 블록은 해제(Detach)해도 돼요. 상단바·하단탭은 먼저 디자인 시스템의 `★top Bar`, `❤︎bottomTab`, `❤︎bottom Bar`를 확인해요.

| 컴포넌트 | 종류 | 언제 | 주요 속성 | key |
|---|---|---|---|---|
| `B-Top_screen` | 세트 | 1depth 상단 (로고·검색·찜·장바구니 + 메뉴 탭) | Device=IOS·AOS, ♥︎Category Bar | `b9b17d3dbc513ac03bd20eac4509696959347baf` |
| `B-Top_detailview` | 세트 | 2depth 상단 (뒤로가기 + 타이틀) | Device, Search Bar | `a141b9931d3201b8d894e78590c59fc543a4e973` |
| `Top Bar_Search` | 세트 | 검색 상단 | Property=AOS·iOS, L_arrow, search, subSearch | `42b5a6ebf3ef360c1a64c88ac914900e89f757f5` |
| `B-Navigation` | 세트 | 하단 탭바 (홈·카테고리·매장·신상톡·마이페이지) | Device, Bottom Bar | `436154ece57fa938f4ce6dc1334aba043a456d3a` |
| `B-Content_Tab` | 세트 | 콘텐츠 탭 | Tab, Tab Option, Fixed tab, Related, tabBar, Text_Dropdown | `795fd4e044f6a47c875cbb42b979864fb0fee0d8` |
| `B-Content_Title` | 세트 | 섹션 타이틀 (좌: 텍스트·숫자·페이지 / 우: 버튼·필터·정렬·체크·스위치·Sponsored) | Type=Type01·Spon+Btn·Type02, L_*/R_* 토글 | `2ac011342614413bfed024e74409de65549967cb` |
| `B-Content_search+filter` | 세트 | 지면 내 검색창 + 필터 바 | search, filter Bar | `8b27433f52460eda63f2a90a98aec10b696c10d5` |
| `B-Info` ⚠️ 미게시 | 세트 | 안내 박스 | Type=Basic·warning, Title, icon, dot, tag, btn | `46cbe4c7ff98aab54bb6d90b591afe1f6b614503` |
| `B-Info_Text` | 단일 | 한 줄 안내 문구 | icon, tag, dot | `23d01b016eda19167fba392d56a6ba2963e8d877` |
| `B-Text_Dropdown` ⚠️ 미게시 | 세트 | 텍스트 드롭다운 (구버전) | sub text | `6efbee962bc68d4e1ec7ef0ca68d4f0872e51ef7` |
| `Text_Dropdown` | 단일 | 텍스트 드롭다운 — `B-Text_Dropdown` 대신 이걸 써요 | — | `6b80205a7fc87d09f43068b08e1129c143082d47` |

> ⚠️ `B-Info`, `B-Text_Dropdown`은 라이브러리에 게시되지 않아 key로 불러오면 실패해요. 드롭다운은 게시된 `Text_Dropdown`을, 안내 문구는 `B-Info_Text`를 써요.
| `Related` | 단일 | 연관 검색어 줄 | — | `1d4bedc9128dc5b42a763dc8b75868d678dae6ab` |
| `B-Portrait Bar` | 세트 | 상태바 | Portrait Bar=AOS·IOS | `ba9c4bf94e920edbd77080962cad1dd2d771997e` |


## 디자인 시스템 기본 컴포넌트

버튼, 칩, 태그, 텍스트 링크, 입력, 체크박스, 모달은 M_Design system Guide에 있어요. 이름 규칙과 사용 규칙은 [design-system/components](../design-system/components.md)를 봐요. 이 컴포넌트들은 **해제하지 않아요.**
