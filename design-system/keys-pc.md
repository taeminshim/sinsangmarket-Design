# PC 자주 쓰는 키 모음

화면을 그릴 때 **매번 검색하지 않고 바로 불러오기 위한 표**예요. 작업하면서 자주 쓰는 PC 컴포넌트·스타일이 생기면 여기에 하나씩 쌓아요 ([추가하는 법](../README.md#자주-쓰는-키-추가하기)).
빌더(PC UI Builder) 컴포넌트 키는 [builder/pc](../builder/pc.md)에 있어요.

> **키가 안 먹으면 검색 결과를 따라요.** 라이브러리가 업데이트되면 키가 바뀔 수 있어요. 표에 없는 컴포넌트는 `includeLibraryKeys`로 PC 디자인 시스템(`lk-fd4e5f06…`, [libraries](../libraries.md))만 남겨서 검색해요.
> PC는 이름 규칙이 모바일과 다른 곳이 있어요 (글자 스타일 `sh3r18`, `h1m40` 등). [foundations](foundations.md)를 같이 봐요.

불러오는 법
- 세트(`component_set`)는 `figma.importComponentSetByKeyAsync(key)`, 단일 컴포넌트는 `importComponentByKeyAsync(key)`
- 스타일은 `figma.importStyleByKeyAsync(key)` 후 `setFillStyleIdAsync` / `setTextStyleIdAsync`로 연결

## 컴포넌트 — 세트

| 이름 | 용도 | 주요 속성 | key |
|---|---|---|---|

## 컴포넌트 — 단일

| 이름 | 용도 | key |
|---|---|---|

## 색 스타일 (Paint)

| 스타일 | 값 | key |
|---|---|---|

## 텍스트 스타일

| 스타일 | 크기(행간) | key |
|---|---|---|

## 쓸 때 주의 (실제 작업에서 겪은 것)

| 상황 | 주의 |
|---|---|
