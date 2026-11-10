# PC 빌더 — PC UI Builder

[PC UI Builder 열기](https://www.figma.com/design/aFam9mIsTVZqNmKdHHYq0f)

화면은 **디자인 시스템에서 시작**해요 (GNB·SNB·FNB·Breadcrumb·버튼·폼은 PC_Design system Guide). 빌더에서는 주로 **상품 썸네일·상품 카드·매장 썸네일**을 가져오고, 표(Table)·템플릿 블록은 필요할 때만 써요.

해상도 대응은 새로 그리지 말고 `Size` variant(1200 / 1440 / 2000)로 바꿔요.
key는 Figma에서 `importComponentByKeyAsync`(단일) / `importComponentSetByKeyAsync`(세트)로 불러올 때 써요.

## 상품 카드 (Product_Card)

| 컴포넌트 | 종류 | 언제 | 주요 속성 | key |
|---|---|---|---|---|
| `standard_card` | 단일 | 기본 상품 카드 | Thumbmail(swap), List item(swap), Show Item, Show Info/btn | `ed643b55f2ac8f770a34c42abbe1bb7efa9aae36` |
| `Thumbnail/Standard 3:4` | 세트 | 3:4 상품 썸네일 | State=Default·Empty_White·Empty_Gary·inactive·soldout, Checkbox·Rank·zzim·Badge·Tag | `723e75935188ad7e2f0db8ae8fecd96d14f79a82` |
| `Thumbnail/Standard 1:1` | 세트 | 1:1 상품 썸네일 | State, Checkbox·Rank·zzim·Badge | `5e506e9c4a701e5dfe31cec6c31e83947c342e91` |
| `Thumbnail/Overlay 3:4` | 세트 | 정보가 이미지 위에 얹히는 3:4 | State, Overlay_Info(swap) | `4b12810ddca49684f3435385d2379f06e9e6cb47` |
| `Thumbnail/Overlay 1:1` | 세트 | 오버레이 1:1 | State, Overlay_Info(swap) | `391613bc5117a90a34ff3c60fc58be5cca6b6b06` |
| `Info/Text/Wide_1Lines` | 세트 | 넓은 그리드, 상품명 1줄 | Size=2000·1440·1200px, ActiveStatus, 가격·할인율·원가·찜수 토글 | `936870228ded9986b4a840b8e9cfe1166a7dd5c1` |
| `Info/Text/Wide_2Lines` | 세트 | 넓은 그리드, 상품명 2줄 | 위와 동일 | `141f7d3fbbdc2284fb2832b699f942928524fc0c` |
| `Info/Text/Tight_1Lines` | 세트 | 촘촘한 그리드, 상품명 1줄 | 위와 동일 | `7092ae215cf1ba4200328f3d08f7a6936a44b791` |
| `Info/Text/Tight_2Lines` | 세트 | 촘촘한 그리드, 상품명 2줄 | 위와 동일 | `d5e7947cac4c35531817b2eccba3d7156307dce3` |
| `Info/Overlay/Wide_1440px` | 세트 | 이미지 위 정보 (넓은 그리드) | Profile Size, ActiveStatus, 항목 토글 | `cae5198b7d63a45db41eb875101ad6a42521f20e` |
| `Info/Overlay/Wide_1200px` | 세트 | 〃 1200 | 〃 | `d7cd240a8fcb0015277287a8025e68d7e0b48235` |
| `Info/Overlay/Wide_2000px` | 세트 | 〃 2000 | 〃 | `1cd1d1d50a020983b1f57e8ad7cc150d0eccb6d5` |
| `Info/Overlay/Tight_1440px` | 세트 | 이미지 위 정보 (촘촘한 그리드) | 〃 | `0d450ac9ae51ad0a659334cb7dde4a10c0b4d128` |
| `Info/Overlay/Tight_1200px` | 세트 | 〃 1200 | 〃 | `4455dfc2384114a7fe061c70b2a8c52980a3f6c7` |
| `Info/Overlay/Tight_2000px` | 세트 | 〃 2000 | 〃 | `a1a1bc736a9ab4b69b64e10ef1f3e1ad5612f9bf` |
| `Info/Store/default` | 세트 | 카드 하단 매장 정보 | Size=2000·1440·1200, Show Tag | `062ff2cfa96a4dc440307b06dd1e753c3c023430` |
| `Info/btn` | 세트 | 카드 하단 버튼 | Size=1440-1200px·2000px | `96ffffa9b5bd9063be0622d393fecf9be92c2dc7` |
| `Showcase_Card` | 세트 | 가로형 상품 요약 카드 | size=1200·1440·2000, ActiveStatus | `837ee8f8b29022f1c386fbb66c12372b26632b98` |
| `Thumbnail_subpage` | 세트 | 서브페이지 썸네일 | 1200·1440·2000px | `addaae1f3a0938ee1d523ac7b82d486191a57044` |
| `thumb_top/zzim` | 세트 | 썸네일 찜 | size=Default·small(100↓) | `8d29b5158b3383e1474c23dd817c3314efa9788d` |
| `thumb_top/alarm` | 세트 | 썸네일 알림 | size=Default·small(100↓) | `52a7229e9181f91b1fbd331123d520295b6787d3` |
| `badge_mbs` | 세트 | 멤버십 배지 | size=18·24·32 | `c1dfc953f6a79203c36b2a83fe0f3d465c360489` |

## 매장 (Store_badge) — ⚠️ 전부 미게시

> ⚠️ 이 섹션 컴포넌트는 PC UI Builder 원본에는 있지만 **라이브러리에 게시되지 않아** 작업 파일에서 key로 불러오면 실패해요. 일부러 숨긴 건지 게시가 빠진 건지 빌더 담당자 확인이 필요해요. 그 전까지 멤버십 배지는 게시된 `badge_mbs`(상품 카드 섹션)를 쓰고, 매장 썸네일이 꼭 필요하면 빌더 원본에서 복사해 와요 (이 경우 라이브러리와 연결되지 않은 로컬 사본이 돼요).

| 컴포넌트 | 종류 | 언제 | 주요 속성 | key |
|---|---|---|---|---|
| `Store_thumb` | 세트 | 매장 썸네일 + 멤버십 배지 | Thumnail=74·72·60·54·50·44·36·32, mbs_badge, thumb_img, thumb_empty | `3bd6b096eadefb25b64987acba94fb27378ffdaf` |
| `Store_thumb_empty` | 세트 | 매장 이미지 없을 때 | size=71↑·70↓, Color=white·gray20·gray30 | `0ec2f7e67f542777545939d12ccacc5a8dbf6b6f` |
| `mbs_badge` | 세트 | 멤버십 배지 | 노출=48↑·47↓·편집, Property=도매·공통·소매 | `714a7592d15575bf416fdb617c8732e978c44a79` |
| `검색결과_매장 리스트` | 단일 | 검색결과 매장 카드 | — | `0ba69ed47cda121a9bc6dd55eb384a29da245486` |
| `마이페이지_내 거래처` | 세트 | 내 거래처 카드 | Property=내 거래처·승인중 거래처 | `b946816db1713be41e3847596ed3b5c8d759c46b` |
| `main_storeinfo_section1` | 세트 | 매장 정보 영역 | size=2000·1440·1200px | `7b791e9b30fafe6336926b3ae9f65e48f442e2bb` |
| `section2_도매홈` | 세트 | 도매홈 섹션 | size=2000·1440·1200px | `b7813770856e9ae2774cecf8c17916b9357484f2` |
| `Thumbnail` (매장) | 세트 | 매장 대표 이미지 | size=1200·2000·1440 | `3a9edd864049b708480f769274d85d7f232b4453` |
| `main_section1_상품리스트_2000px` | 세트 | 매장 메인 상품 리스트 | size=2000px·1200px | `7892ecf0cbd11747fe7ae6fc1b288a896acc8137` |
| `소매_프리미엄도매홈` | 단일 | 소매 프리미엄 도매홈 영역 (슬롯: 컨텐츠, list) | — | `27fda273c09721802d2ae484666b20914335d842` |

> 빌더 파일 안에 `마이페이지_내 거래처`가 두 개 있어요. 위 키는 노드 2347:29766 쪽이에요. 다른 하나는 `d18baeb85eb44df2a64f260713bd25ed8deae7b3`(2363:41122)이니 어느 쪽이 최신인지 빌더 담당자 확인이 필요해요.

## 목록 (Table) — 마이페이지 표

| 컴포넌트 | 언제 | key |
|---|---|---|
| `B-some/table_list/payment` | 결제 내역 표 | `364668b10ace621d5c7883448675cd0f19c686f5` |
| `B-some/table_list/usage` | 이용 내역 표 | `63319b7d7c66cb546a222bada405cc4c46e256ac` |
| `B-some/table_list/staff` | 직원 관리 표 | `166077f7cd65a05f216fe97afe6c501d87467728` |
| `B-some/table_list/history_1` · `_2` · `_3` | 히스토리 표 | `4f7dffe1eab14ad9672a4ac2d10f3a22ac275f17` · `f359ae9c16c1498fcdd7f6f8d27809b20c3177bd` · `8eb366102c78ced065eaa2999c54606ad7d36643` |
| `B-some_/table_order/item_1` · `B-some/table_order/item_2` | 주문 상품 표 | `a7f8101944510952aee26097d30c3eb0f306b4a7` · `dfbb9e3e90a040716a0b11fd72c5862409b9a9a2` |
| `B-some/table_order/store_2` · `_3` | 매장별 주문 표 | `d7f9539eeacea00e0b6fdc9269fa7616a2cae29a` · `ef0b888bc283802727df713fbe80726191a87835` |
| `B-some/table_row/order_1` · `_2` · `_4` | 주문 행 | `4c2cdf7833f244949948aa8b55be1541656cc2bb` · `8466c534ac36d3fc3654d6b3297bcb443913a3a4` · `dbcc76993197cfbf93e63a574a154061ab262387` |

## Footer

| 컴포넌트 | 언제 | 주요 속성 | key |
|---|---|---|---|
| `Footer_로그인전후` | 일반 지면 하단 | 노출영역=로그인전후·로그인후·로그인전, 국가=kr·en·jp·cn, 해상도=360~·1024~·1200~·1440~, 도소매구분=소매·도매 | `2189832c674ff8d4ea2b82749f7acb0f390f99f6` |
| `Footer_소개페이지` | 소개 페이지 하단 | 국가, 해상도 | `ef7b0f10ba13c36a4d1a831662f9d9aa5f316dbd` |
| `Footer` | 구버전 통합 푸터 | 노출영역, 국가, 타입=PC·Mo | `8b68f36e3de42928f7817fb3f49d9b0c56172219` |

## 디자인 시스템 기본 컴포넌트

버튼, 칩, 태그, 텍스트 링크, 입력, 체크박스, 모달은 PC_Design system Guide에 있어요. 이름 규칙과 사용 규칙은 [design-system/components](../design-system/components.md)를 봐요. 이 컴포넌트들은 **해제하지 않아요.**
