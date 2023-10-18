<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Content-based рекомендательная система для сервиса Своё|Село от Россельхозбанка</title><style>
/* cspell:disable-file */
/* webkit printing magic: print all background colors */
html {
	-webkit-print-color-adjust: exact;
}
* {
	box-sizing: border-box;
	-webkit-print-color-adjust: exact;
}

html,
body {
	margin: 0;
	padding: 0;
}
@media only screen {
	body {
		margin: 2em auto;
		max-width: 900px;
		color: rgb(55, 53, 47);
	}
}

body {
	line-height: 1.5;
	white-space: pre-wrap;
}

a,
a.visited {
	color: inherit;
	text-decoration: underline;
}

.pdf-relative-link-path {
	font-size: 80%;
	color: #444;
}

h1,
h2,
h3 {
	letter-spacing: -0.01em;
	line-height: 1.2;
	font-weight: 600;
	margin-bottom: 0;
}

.page-title {
	font-size: 2.5rem;
	font-weight: 700;
	margin-top: 0;
	margin-bottom: 0.75em;
}

h1 {
	font-size: 1.875rem;
	margin-top: 1.875rem;
}

h2 {
	font-size: 1.5rem;
	margin-top: 1.5rem;
}

h3 {
	font-size: 1.25rem;
	margin-top: 1.25rem;
}

.source {
	border: 1px solid #ddd;
	border-radius: 3px;
	padding: 1.5em;
	word-break: break-all;
}

.callout {
	border-radius: 3px;
	padding: 1rem;
}

figure {
	margin: 1.25em 0;
	page-break-inside: avoid;
}

figcaption {
	opacity: 0.5;
	font-size: 85%;
	margin-top: 0.5em;
}

mark {
	background-color: transparent;
}

.indented {
	padding-left: 1.5em;
}

hr {
	background: transparent;
	display: block;
	width: 100%;
	height: 1px;
	visibility: visible;
	border: none;
	border-bottom: 1px solid rgba(55, 53, 47, 0.09);
}

img {
	max-width: 100%;
}

@media only print {
	img {
		max-height: 100vh;
		object-fit: contain;
	}
}

@page {
	margin: 1in;
}

.collection-content {
	font-size: 0.875rem;
}

.column-list {
	display: flex;
	justify-content: space-between;
}

.column {
	padding: 0 1em;
}

.column:first-child {
	padding-left: 0;
}

.column:last-child {
	padding-right: 0;
}

.table_of_contents-item {
	display: block;
	font-size: 0.875rem;
	line-height: 1.3;
	padding: 0.125rem;
}

.table_of_contents-indent-1 {
	margin-left: 1.5rem;
}

.table_of_contents-indent-2 {
	margin-left: 3rem;
}

.table_of_contents-indent-3 {
	margin-left: 4.5rem;
}

.table_of_contents-link {
	text-decoration: none;
	opacity: 0.7;
	border-bottom: 1px solid rgba(55, 53, 47, 0.18);
}

table,
th,
td {
	border: 1px solid rgba(55, 53, 47, 0.09);
	border-collapse: collapse;
}

table {
	border-left: none;
	border-right: none;
}

th,
td {
	font-weight: normal;
	padding: 0.25em 0.5em;
	line-height: 1.5;
	min-height: 1.5em;
	text-align: left;
}

th {
	color: rgba(55, 53, 47, 0.6);
}

ol,
ul {
	margin: 0;
	margin-block-start: 0.6em;
	margin-block-end: 0.6em;
}

li > ol:first-child,
li > ul:first-child {
	margin-block-start: 0.6em;
}

ul > li {
	list-style: disc;
}

ul.to-do-list {
	padding-inline-start: 0;
}

ul.to-do-list > li {
	list-style: none;
}

.to-do-children-checked {
	text-decoration: line-through;
	opacity: 0.375;
}

ul.toggle > li {
	list-style: none;
}

ul {
	padding-inline-start: 1.7em;
}

ul > li {
	padding-left: 0.1em;
}

ol {
	padding-inline-start: 1.6em;
}

ol > li {
	padding-left: 0.2em;
}

.mono ol {
	padding-inline-start: 2em;
}

.mono ol > li {
	text-indent: -0.4em;
}

.toggle {
	padding-inline-start: 0em;
	list-style-type: none;
}

/* Indent toggle children */
.toggle > li > details {
	padding-left: 1.7em;
}

.toggle > li > details > summary {
	margin-left: -1.1em;
}

.selected-value {
	display: inline-block;
	padding: 0 0.5em;
	background: rgba(206, 205, 202, 0.5);
	border-radius: 3px;
	margin-right: 0.5em;
	margin-top: 0.3em;
	margin-bottom: 0.3em;
	white-space: nowrap;
}

.collection-title {
	display: inline-block;
	margin-right: 1em;
}

.page-description {
    margin-bottom: 2em;
}

.simple-table {
	margin-top: 1em;
	font-size: 0.875rem;
	empty-cells: show;
}
.simple-table td {
	height: 29px;
	min-width: 120px;
}

.simple-table th {
	height: 29px;
	min-width: 120px;
}

.simple-table-header-color {
	background: rgb(247, 246, 243);
	color: black;
}
.simple-table-header {
	font-weight: 500;
}

time {
	opacity: 0.5;
}

.icon {
	display: inline-block;
	max-width: 1.2em;
	max-height: 1.2em;
	text-decoration: none;
	vertical-align: text-bottom;
	margin-right: 0.5em;
}

img.icon {
	border-radius: 3px;
}

.user-icon {
	width: 1.5em;
	height: 1.5em;
	border-radius: 100%;
	margin-right: 0.5rem;
}

.user-icon-inner {
	font-size: 0.8em;
}

.text-icon {
	border: 1px solid #000;
	text-align: center;
}

.page-cover-image {
	display: block;
	object-fit: cover;
	width: 100%;
	max-height: 30vh;
}

.page-header-icon {
	font-size: 3rem;
	margin-bottom: 1rem;
}

.page-header-icon-with-cover {
	margin-top: -0.72em;
	margin-left: 0.07em;
}

.page-header-icon img {
	border-radius: 3px;
}

.link-to-page {
	margin: 1em 0;
	padding: 0;
	border: none;
	font-weight: 500;
}

p > .user {
	opacity: 0.5;
}

td > .user,
td > time {
	white-space: nowrap;
}

input[type="checkbox"] {
	transform: scale(1.5);
	margin-right: 0.6em;
	vertical-align: middle;
}

p {
	margin-top: 0.5em;
	margin-bottom: 0.5em;
}

.image {
	border: none;
	margin: 1.5em 0;
	padding: 0;
	border-radius: 0;
	text-align: center;
}

.code,
code {
	background: rgba(135, 131, 120, 0.15);
	border-radius: 3px;
	padding: 0.2em 0.4em;
	border-radius: 3px;
	font-size: 85%;
	tab-size: 2;
}

code {
	color: #eb5757;
}

.code {
	padding: 1.5em 1em;
}

.code-wrap {
	white-space: pre-wrap;
	word-break: break-all;
}

.code > code {
	background: none;
	padding: 0;
	font-size: 100%;
	color: inherit;
}

blockquote {
	font-size: 1.25em;
	margin: 1em 0;
	padding-left: 1em;
	border-left: 3px solid rgb(55, 53, 47);
}

.bookmark {
	text-decoration: none;
	max-height: 8em;
	padding: 0;
	display: flex;
	width: 100%;
	align-items: stretch;
}

.bookmark-title {
	font-size: 0.85em;
	overflow: hidden;
	text-overflow: ellipsis;
	height: 1.75em;
	white-space: nowrap;
}

.bookmark-text {
	display: flex;
	flex-direction: column;
}

.bookmark-info {
	flex: 4 1 180px;
	padding: 12px 14px 14px;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}

.bookmark-image {
	width: 33%;
	flex: 1 1 180px;
	display: block;
	position: relative;
	object-fit: cover;
	border-radius: 1px;
}

.bookmark-description {
	color: rgba(55, 53, 47, 0.6);
	font-size: 0.75em;
	overflow: hidden;
	max-height: 4.5em;
	word-break: break-word;
}

.bookmark-href {
	font-size: 0.75em;
	margin-top: 0.25em;
}

.sans { font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol"; }
.code { font-family: "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace; }
.serif { font-family: Lyon-Text, Georgia, ui-serif, serif; }
.mono { font-family: iawriter-mono, Nitti, Menlo, Courier, monospace; }
.pdf .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK JP'; }
.pdf:lang(zh-CN) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK SC'; }
.pdf:lang(zh-TW) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK TC'; }
.pdf:lang(ko-KR) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK KR'; }
.pdf .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.pdf .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK JP'; }
.pdf:lang(zh-CN) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK SC'; }
.pdf:lang(zh-TW) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK TC'; }
.pdf:lang(ko-KR) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK KR'; }
.pdf .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.highlight-default {
	color: rgba(55, 53, 47, 1);
}
.highlight-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(120, 119, 116, 1);
}
.highlight-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(159, 107, 83, 1);
}
.highlight-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(217, 115, 13, 1);
}
.highlight-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 145, 47, 1);
}
.highlight-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(68, 131, 97, 1);
}
.highlight-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(51, 126, 169, 1);
}
.highlight-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(144, 101, 176, 1);
}
.highlight-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.highlight-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(212, 76, 71, 1);
}
.highlight-gray_background {
	background: rgba(241, 241, 239, 1);
}
.highlight-brown_background {
	background: rgba(244, 238, 238, 1);
}
.highlight-orange_background {
	background: rgba(251, 236, 221, 1);
}
.highlight-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.highlight-teal_background {
	background: rgba(237, 243, 236, 1);
}
.highlight-blue_background {
	background: rgba(231, 243, 248, 1);
}
.highlight-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.highlight-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.highlight-red_background {
	background: rgba(253, 235, 236, 1);
}
.block-color-default {
	color: inherit;
	fill: inherit;
}
.block-color-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(120, 119, 116, 1);
}
.block-color-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(159, 107, 83, 1);
}
.block-color-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(217, 115, 13, 1);
}
.block-color-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 145, 47, 1);
}
.block-color-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(68, 131, 97, 1);
}
.block-color-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(51, 126, 169, 1);
}
.block-color-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(144, 101, 176, 1);
}
.block-color-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.block-color-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(212, 76, 71, 1);
}
.block-color-gray_background {
	background: rgba(241, 241, 239, 1);
}
.block-color-brown_background {
	background: rgba(244, 238, 238, 1);
}
.block-color-orange_background {
	background: rgba(251, 236, 221, 1);
}
.block-color-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.block-color-teal_background {
	background: rgba(237, 243, 236, 1);
}
.block-color-blue_background {
	background: rgba(231, 243, 248, 1);
}
.block-color-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.block-color-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.block-color-red_background {
	background: rgba(253, 235, 236, 1);
}
.select-value-color-interactiveBlue { background-color: rgba(35, 131, 226, .07); }
.select-value-color-pink { background-color: rgba(245, 224, 233, 1); }
.select-value-color-purple { background-color: rgba(232, 222, 238, 1); }
.select-value-color-green { background-color: rgba(219, 237, 219, 1); }
.select-value-color-gray { background-color: rgba(227, 226, 224, 1); }
.select-value-color-translucentGray { background-color: rgba(255, 255, 255, 0.0375); }
.select-value-color-orange { background-color: rgba(250, 222, 201, 1); }
.select-value-color-brown { background-color: rgba(238, 224, 218, 1); }
.select-value-color-red { background-color: rgba(255, 226, 221, 1); }
.select-value-color-yellow { background-color: rgba(253, 236, 200, 1); }
.select-value-color-blue { background-color: rgba(211, 229, 239, 1); }
.select-value-color-pageGlass { background-color: undefined; }
.select-value-color-washGlass { background-color: undefined; }

.checkbox {
	display: inline-flex;
	vertical-align: text-bottom;
	width: 16;
	height: 16;
	background-size: 16px;
	margin-left: 2px;
	margin-right: 5px;
}

.checkbox-on {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22%2358A9D7%22%2F%3E%0A%3Cpath%20d%3D%22M6.71429%2012.2852L14%204.9995L12.7143%203.71436L6.71429%209.71378L3.28571%206.2831L2%207.57092L6.71429%2012.2852Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E");
}

.checkbox-off {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20x%3D%220.75%22%20y%3D%220.75%22%20width%3D%2214.5%22%20height%3D%2214.5%22%20fill%3D%22white%22%20stroke%3D%22%2336352F%22%20stroke-width%3D%221.5%22%2F%3E%0A%3C%2Fsvg%3E");
}
	
</style></head><body><article id="fbb23b8a-6f7f-435d-937b-5624b6f0cfa2" class="page sans"><header><div class="page-header-icon undefined"><span class="icon">💵</span></div><h1 class="page-title">Content-based рекомендательная система для сервиса Своё|Село от Россельхозбанка</h1><p class="page-description"></p></header><div class="page-body"><p id="46af4684-6fe8-4939-8b77-5740ed12189b" class="">Было предложено реализовать систему рекомендаций для данного сервиса.  Как итог хотим получить набор категорий товаров, подходящих для избранной категории услуг и наоборот. В идеале же хочется получать рекомендации конкретных(!) товаров к конкретным(!) услугам и наоборот. </p><h2 id="22ac3c57-e1d5-414c-9081-afe81d46a92e" class="">Шаг 1. Изучение предложенного каталога</h2><p id="d32d58ef-301d-4c1a-842a-a65681d481ae" class="">Каталог выглядит следующим образом:</p><figure id="8425feaf-e90e-44ee-a9f4-6ebd20b6f99c" class="image"><a href="Content-based%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%20fbb23b8a6f7f435d937b5624b6f0cfa2/Untitled.png"><img style="width:1336px" src="Content-based%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%20fbb23b8a6f7f435d937b5624b6f0cfa2/Untitled.png"/></a></figure><p id="ff2b7d29-3cd4-41ce-873f-88433ee09a2d" class="">Нас интересуют надкатегории “Строительство”, “Ремонт” и “Строительные материалы”. Две первые надкатегории можно объединить до строительных услуг. </p><p id="b1768569-a25e-473a-9e1c-4b958caf7592" class="">Разберемся с устройством каталога на примере надкатегории “Ремонт”. Она состоит из следующих категорий:</p><figure id="49e99b11-06b5-4a1a-b5e8-cab8bba1a3b5" class="image"><a href="Content-based%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%20fbb23b8a6f7f435d937b5624b6f0cfa2/Untitled%201.png"><img style="width:336px" src="Content-based%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%20fbb23b8a6f7f435d937b5624b6f0cfa2/Untitled%201.png"/></a></figure><p id="973d42fa-685f-4f13-82aa-d0fa546cd6f7" class="">Которые, в свою очередь, состоят из подкатегорий:</p><figure id="edb3dd38-7132-41b1-a1a2-ac0b940bab50" class="image"><a href="Content-based%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%20fbb23b8a6f7f435d937b5624b6f0cfa2/Untitled%202.png"><img style="width:330px" src="Content-based%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%20fbb23b8a6f7f435d937b5624b6f0cfa2/Untitled%202.png"/></a></figure><p id="52397559-21d2-438a-9925-d3cdfb2d154c" class="">Которые уже никуда не ведут. </p><figure id="878f4ae3-302e-4bc3-9258-cb09e984e030" class="image"><a href="Content-based%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%20fbb23b8a6f7f435d937b5624b6f0cfa2/Untitled%203.png"><img style="width:322px" src="Content-based%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%20fbb23b8a6f7f435d937b5624b6f0cfa2/Untitled%203.png"/></a></figure><p id="39ac0fac-1ce6-4d78-b878-68983070dca7" class="">Теперь изучим карточку товара:</p><figure id="a69875e3-27bb-47be-b76a-326d5319e7d5" class="image"><a href="Content-based%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%20fbb23b8a6f7f435d937b5624b6f0cfa2/Untitled%204.png"><img style="width:961px" src="Content-based%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%20fbb23b8a6f7f435d937b5624b6f0cfa2/Untitled%204.png"/></a></figure><p id="f4ff87b6-6b73-42ae-9c10-dfa3231310e0" class="">Если на нее кликнуть, то откроется ещё более подробная версия:</p><figure id="a2d3270f-17a6-4536-989d-9b2e4304cf29" class="image"><a href="Content-based%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%20fbb23b8a6f7f435d937b5624b6f0cfa2/Untitled%205.png"><img style="width:1005px" src="Content-based%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%20fbb23b8a6f7f435d937b5624b6f0cfa2/Untitled%205.png"/></a></figure><p id="c9e0e7d8-673e-40e6-a09b-549fdac7d609" class="">К сожалению, не у всех карточек есть подробное описание:</p><figure id="0f90d3cf-103a-4000-8819-fda22ca5eedb" class="image"><a href="Content-based%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%20fbb23b8a6f7f435d937b5624b6f0cfa2/Untitled%206.png"><img style="width:1466px" src="Content-based%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%B0%20fbb23b8a6f7f435d937b5624b6f0cfa2/Untitled%206.png"/></a></figure><p id="4f630ad2-a719-4f17-8f71-45204d2922f3" class="">Подробной аналитики по продажам предоставлено не было, так что с настоящего момента исходим из того, что нужно реализовать т.н. “Холодный старт”, основываясь на данных с сайта, а аналитику для рекомендаций собирать и применять находу, заранее подготовив план действий по работе с ней.</p><p id="1fee40ee-650c-4266-b753-395fd0fb5688" class="">
</p><h2 id="c5023f94-7c30-467e-b862-a8991087f483" class="">Шаг 2-3. Собираем данные и определяем методы рекомендации, параллельно автоматизируя</h2><p id="51726c2f-bdac-4a04-8af8-36518027cb4c" class="">Было бы круто иметь все данные под рукой, без необходимости заходить на сайт и вручную собирать какие-то данные. Для этого был написан специальный скрипт <a href="https://github.com/MeganJard/RSHB_Project_Bogdanov_Jaroslav/blob/main/parser.py">parser.py</a>. Он возвращает данные в удобном для обработке виде(подходит любая ссылка из каталога):</p><pre id="5030885a-f883-426e-92bd-c4fcb851d388" class="code"><code>{
&quot;Покраска древесины~0~https://svoe-selo.ru/services-catalog/pokraska-drevesiny&quot;:
 &quot;Покраска \n
	Покрытие древесины защитными маслами \n
	Паропроницаемость масла-воска оставляет дереву возможность дышать. 
		Состав не влияет на текстуру дерева, легко наносится, при добавлении колера – 
		меняет цвет поверхности. Покрытие устойчиво к влажности, перепадам температуры,
		пожаробезопасно. Защита дерева происходит не только снаружи, состав проникает 
		внутрь и защищает дерево изнутри. При необходимости точечного ремонта повторное
		покрытие потребуется только в отремонтированной области. \n \n
	Преимущества защиты пиломатериалов:\n
	1. безопасность; \n 
	2. сохранение эстетичного древесного рисунка; \n
	3. матовый блеск; \n 
	4. бархатистость на ощупь; \n
	5. простота нанесения; \n
	6. быстрая реставрация поврежденного участка; \n 
	7. невысокая цена покраски дерева маслом \n\n 
	
	Есть собственное производство в г. Москва, так же есть склад с большим 
		количеством пиломатериала разных пород древесины: сосна, лиственница, ясень,
		дуб, акация и тд.\n
	Можем оказать малярные услуги с Вашим материалом или же предоставить свой материал. \n
	Так же предоставляем гарантию в зависимости от оказанных услуг от 1 года. \n 
	Работы выполняются также по индивидуальным запросам клиента. \n\n 
	
	Работаем как с НДС так и по наличному расчету.\n\n&quot;, 
... }</code></pre><p id="3610e83f-aef8-4ea3-9a0e-b36a34034ce2" class="">
</p><p id="f8d58579-76f8-4b5f-86e2-a202f9a7a9f7" class="">Рекомендации будут построены следующим образом. Сначала вручную будут сопоставлены подкатегории товаров и подкатегории услуг, затем каждый товар будет проанализирован, разбит на теги, и по наибольшему пересечению тегов между товарами из подходящих категорий будут выбираться подходящие товары.</p><p id="35787bce-4961-43c3-b752-8665894e4be1" class="">Таблица сопоставления подкатегорий следующая:</p><div id="15228dff-646d-4705-90a5-6b31f4fa80b2" class="collection-content"><h4 class="collection-title">Соответствие категорий товаров и услуг</h4><table class="collection-content"><thead><tr><th><span class="icon property-icon"><img src="https://www.notion.so/icons/barcode_gray.svg" style="width:14px;height:14px"/></span>Товар</th><th><span class="icon property-icon"><img src="https://www.notion.so/icons/ambulance_gray.svg" style="width:14px;height:14px"/></span>Услуга</th></tr></thead><tbody><tr id="db09c445-897f-4fc3-8788-cbd06dd9b867"><td class="cell-title"><a href="https://www.notion.so/db09c445897f4fc38788cbd06dd9b867?pvs=21">Песок, щебень</a></td><td class="cell-IQ`A">Фундамент, Возведение стен, Перекрытия, Лестницы, Укладка полов</td></tr><tr id="9b8c9ade-1645-470c-82fe-9c3171402a5e"><td class="cell-title"><a href="https://www.notion.so/9b8c9ade1645470c82fe9c3171402a5e?pvs=21">Бетон</a></td><td class="cell-IQ`A">Фундамент, Возведение стен, Перерытия, Лестницы, Монтаж фасадов, Отделка стен, Укладка полов</td></tr><tr id="5aaf5510-3e96-4ed1-ae0b-274021142287"><td class="cell-title"><a href="https://www.notion.so/5aaf55103e964ed1ae0b274021142287?pvs=21">Кирпич, керамоблоки</a></td><td class="cell-IQ`A">Фундамент, Возведение стен, Перерытия, Крыша, Лестницы</td></tr><tr id="aea2b6a1-8740-4c8e-870c-72b6cc384fa9"><td class="cell-title"><a href="https://www.notion.so/aea2b6a187404c8e870c72b6cc384fa9?pvs=21">Газосиликат, газобетон</a></td><td class="cell-IQ`A">Фундамент, Возведение стен, Перерытия, Крыша, Лестницы</td></tr><tr id="b9acd5ad-4cf8-487f-ab6d-48f18840252e"><td class="cell-title"><a href="https://www.notion.so/b9acd5ad4cf8487fab6d48f18840252e?pvs=21">СИП-панели</a></td><td class="cell-IQ`A">Возведение стен, Перерытия</td></tr><tr id="95ec9ed2-5b5f-40e4-a074-e7bafa392c3c"><td class="cell-title"><a href="https://www.notion.so/95ec9ed25b5f40e4a074e7bafa392c3c?pvs=21">Панели</a></td><td class="cell-IQ`A">Возведение стен, Лестницы, Отделка наружних стен, Монтаж фасадов, Отделка стен</td></tr><tr id="066b9c88-e3fe-4a57-aa52-c145f98d55a2"><td class="cell-title"><a href="https://www.notion.so/066b9c88e3fe4a57aa52c145f98d55a2?pvs=21">Для внутренней отделки</a></td><td class="cell-IQ`A">Возведение стен, Лестницы, Отделка стен</td></tr><tr id="c1c248d0-6043-4b4f-a844-528cee42bc30"><td class="cell-title"><a href="https://www.notion.so/c1c248d060434b4fa844528cee42bc30?pvs=21">Для наружной отделки</a></td><td class="cell-IQ`A">Возведение стен, Лестницы, Отделка наружних стен, Монтаж фасадов</td></tr><tr id="f92212aa-be5b-4240-9c0f-5b3cecef8282"><td class="cell-title"><a href="https://www.notion.so/f92212aabe5b42409c0f5b3cecef8282?pvs=21">Плитка и принадлежности для укладки</a></td><td class="cell-IQ`A">Отделка наружних стен, Монтаж фасадов, Отделка стен, Укладка полов, Укладка плитки</td></tr><tr id="a722403c-5ce7-4084-87d4-3d90c453b0b9"><td class="cell-title"><a href="https://www.notion.so/a722403c5ce7408487d43d90c453b0b9?pvs=21">Сухие смеси и грунтовки</a></td><td class="cell-IQ`A">Отделка наружних стен, Монтаж фасадов, Укладка полов, Покраска</td></tr><tr id="f0d71711-0c84-42b2-bc88-a725707bd973"><td class="cell-title"><a href="https://www.notion.so/f0d717110c8442b2bc88a725707bd973?pvs=21">Металлоконструкции</a></td><td class="cell-IQ`A">Возведение стен</td></tr><tr id="ad5ca745-d77f-442e-909d-4dc10510f1d9"><td class="cell-title"><a href="https://www.notion.so/ad5ca745d77f442e909d4dc10510f1d9?pvs=21">Профлисты</a></td><td class="cell-IQ`A">Крыша</td></tr><tr id="0553a4aa-499b-4437-8eeb-11eab67a146c"><td class="cell-title"><a href="https://www.notion.so/0553a4aa499b44378eeb11eab67a146c?pvs=21">Сетка</a></td><td class="cell-IQ`A">Фундамент, Возведение стен, Отделка наружних стен, Монтаж фасадов, Отделка стен, Укладка полов</td></tr><tr id="df16ab1b-1970-4bec-8153-82d771f97da4"><td class="cell-title"><a href="https://www.notion.so/df16ab1b19704bec815382d771f97da4?pvs=21">Эмали и лаки</a></td><td class="cell-IQ`A">Возведение стен, Отделка наружних стен, Монтаж фасадов, Отделка стен, Укладка полов, Покраска</td></tr><tr id="f6cb2b13-0a6f-463c-ac92-8cdcc81fa077"><td class="cell-title"><a href="https://www.notion.so/f6cb2b130a6f463cac928cdcc81fa077?pvs=21">Краски для внутренних работ</a></td><td class="cell-IQ`A">Возведение стен, Отделка стен, Покраска</td></tr><tr id="783c6dda-ff31-46b8-ab0f-28974caf0b91"><td class="cell-title"><a href="https://www.notion.so/783c6ddaff3146b8ab0f28974caf0b91?pvs=21">Краски для наружных работ</a></td><td class="cell-IQ`A">Возведение стен, Отделка наружних стен, Монтаж фасадов, Покраска</td></tr><tr id="61c215a4-97ad-49ef-beb2-bbd07761e226"><td class="cell-title"><a href="https://www.notion.so/61c215a497ad49efbeb2bbd07761e226?pvs=21">Декоративные обои</a></td><td class="cell-IQ`A">Возведение стен, Отделка стен</td></tr><tr id="fe7a46f1-6381-4383-b366-fd5dec80c48b"><td class="cell-title"><a href="https://www.notion.so/fe7a46f163814383b366fd5dec80c48b?pvs=21">Обои под покраску</a></td><td class="cell-IQ`A">Возведение стен, Отделка стен, Покраска</td></tr><tr id="8a60701f-c739-4cab-97a1-e1ce1058a825"><td class="cell-title"><a href="https://www.notion.so/8a60701fc7394cab97a1e1ce1058a825?pvs=21">Окна</a></td><td class="cell-IQ`A">Возведение стен, Установка окон, Жалюзи</td></tr><tr id="180d16e9-8ad0-44a5-902f-0cfa0190f70e"><td class="cell-title"><a href="https://www.notion.so/180d16e98ad044a5902f0cfa0190f70e?pvs=21">Двери</a></td><td class="cell-IQ`A">Отделка наружних стен, Монтаж фасадов, Отделка стен, Установка дверей</td></tr><tr id="52c01ad8-d22c-4479-aa85-b88a946ff4b4"><td class="cell-title"><a href="https://www.notion.so/52c01ad8d22c4479aa85b88a946ff4b4?pvs=21">Брус, бревно</a></td><td class="cell-IQ`A">Возведение стен, Перекрытия, Лестницы, Установка дверей,</td></tr></tbody></table><br/><br/></div><p id="130f850c-dd40-49e6-97a3-11ab26400796" class="">На обработке данных остановимся поподробнее. Полная версия ноутбука <a href="https://github.com/MeganJard/RSHB_Project_Bogdanov_Jaroslav/blob/main/Data_processing.ipynb">здесь</a>.</p><p id="527b07fc-02bb-41b4-820f-8726bb5f2cc0" class="">Для начала скачаем пакеты, которые Colab не предоставляет по умолчанию, затем подключим нужные библиотеки, подгрузим нужные данные и инициализируем необходимые объекты для обработки текстовых данных:</p><pre id="22c82ffd-e62c-49f4-aa73-4a1e5238d9d0" class="code"><code>#!pip install pymorphy2
     
import nltk
import re
import pymorphy2
import json

nltk.download(&quot;stopwords&quot;) # стоп слова
nltk.download(&#x27;wordnet&#x27;) # проводит лемматизацию
nltk.download(&#x27;averaged_perceptron_tagger&#x27;) #тэги для английских слов
nltk.download(&#x27;averaged_perceptron_tagger_ru&#x27;) #для русских
nltk.download(&#x27;punkt&#x27;) #токенайзер
from nltk.corpus import stopwords

morph = pymorphy2.MorphAnalyzer()
lemmatize = nltk.WordNetLemmatizer()</code></pre><p id="d41fffbd-ac1f-4ade-89cb-d6738a79eca6" class="">Теперь заполним все стартовые данные, приведя их к удобному виду, заодно объединим таблицы со стротельством и ремонтом:</p><pre id="5da0f019-c3cf-4594-bac6-38310767d1d4" class="code"><code>towar_uslugi = {}
uslugi_towar = {}
all_uslugi = set()
with open(&#x27;/content/materials_fully.json&#x27;) as json_file:
    materials_data = json.load(json_file)
with open(&#x27;/content/stroyka_fully.json&#x27;) as json_file:
    stroyka_data = json.load(json_file)
with open(&#x27;/content/remont_fully.json&#x27;) as json_file:
    stroyka_data |= json.load(json_file)

with open(r&#x27;/content/Соответствие категорий товаров и услуг.csv&#x27;, encoding=&#x27;utf-8&#x27;) as f:
    for line in f:
        line = line.replace(&#x27;\n&#x27;, &#x27;&#x27;)
        towar = line.split(&#x27;;&#x27;)[0]
        uslugi = line.split(&#x27;;&#x27;)[1].split(&#x27;, &#x27;)
        towar_uslugi[towar] = uslugi


# Сделаем из таблицы товар-&gt;услуги таблицу услуга-&gt;товары

for towar in towar_uslugi:
    for usluga in towar_uslugi[towar]:
        all_uslugi.add(usluga)

for usluga in list(all_uslugi):
    uslugi_towar[usluga] = []
    for towar in towar_uslugi:
        if usluga in towar_uslugi[towar]:
            uslugi_towar[usluga].append(towar)</code></pre><p id="a28df906-9054-4786-8600-0bf189613f04" class="">
Также стоит добавить дополнительные стопслова, которые помешают выделять токены из описаний товаров:</p><pre id="158daaec-1052-41ce-a387-26117afaabbd" class="code"><code>custom_stopwords = open(&#x27;/content/custom_stopwords.txt&#x27;).read().replace(&#x27; &#x27;, &#x27;&#x27;).replace(&#x27;\t&#x27;, &#x27;&#x27;).split(&#x27;\n&#x27;)</code></pre><p id="d2611c74-f6d1-4ecd-b580-ab8e50e58c73" class="">
</p><p id="c37d85f5-dbf4-4f08-8bab-e79873607931" class="">Инициализируем функцию токенизации. Она принимает в себя текст и отдает готовые токены:</p><pre id="fe1670b7-14c2-4641-810f-90dd5098c107" class="code"><code>def get_tokens(input):
  input = input.lower()
  regular = r&#x27;[\*+\#+\№\&quot;\-+\+\=+\?+\&amp;\^\.+\;\,+\&gt;+\/+\:\+\–+]&#x27; #убираем все не-буквы
  regular_url = r&#x27;(http\S+)|(www\S+)|([\w\d]+www\S+)|([\w\d]+http\S+)&#x27; #убираем все ссылки
  input = re.sub(regular, &#x27;&#x27;, input)
  input = re.sub(regular_url, r&#x27;URL&#x27;, input)
  input = re.sub(r&#x27;(\d+\s\d+)|(\d+)&#x27;,&#x27; NUM &#x27;, input) # убираем числа
  input = re.sub(r&#x27;\s+&#x27;, &#x27; &#x27;, input)
  text = nltk.word_tokenize(input, language=&#x27;russian&#x27;) #токенизация встроенными средствами
  #преобразуем слова в начальную форму
	text = [lemmatize.lemmatize(word) for word in text]
  filtered_words = [word for word in text if morph.parse(word)[0].normal_form not in \ 
		stopwords.words(&#x27;russian&#x27;)+custom_stopwords]
  #Каждое слово заменяем на пару вида слово: его часть речи
	tagged = nltk.pos_tag(filtered_words, lang=&#x27;rus&#x27;)
  for i in range(len(tagged)):
		#убираем нерусские слова, числа, глаголы и прилагательные
    if tagged[i][1] in [&#x27;NONLEX&#x27;, &#x27;INTJ&#x27;, &#x27;V&#x27;, &#x27;ADV&#x27;]:
      tagged[i] = &#x27;&#x27;
  tagged = list(filter((&#x27;&#x27;).__ne__, tagged))
  for i in range(len(tagged)):
    tagged[i] = morph.parse(tagged[i][0])[0].normal_form

  return tagged</code></pre><p id="c123446a-dfa9-4f2a-ba4a-eb0d99ef1005" class="">
</p><p id="3dc0436a-89c9-4954-b690-012f3ff3a467" class="">Применим эту функцию, получим словарь с удобными данными:</p><pre id="7d867d65-ba4e-4d51-a188-172b9b7420d6" class="code"><code>stroyka_dict = {}
materials_dict = {}

for item in stroyka_data:
  item_dict = {}
  item_dict[&#x27;url&#x27;] = item.split(&#x27;~&#x27;)[2]
  item_dict[&#x27;name&#x27;] = list(set(get_tokens(item.split(&#x27;~&#x27;)[0])))
  item_dict[&#x27;opis&#x27;] = list(set(get_tokens(stroyka_data[item])))
  item_dict[&#x27;real_name&#x27;] = item.split(&#x27;~&#x27;)[0]
  item_dict[&#x27;categ&#x27;] = stroyka_data[item].split(&#x27;\n&#x27;)[0]
  stroyka_dict[item.split(&#x27;~&#x27;)[1]] = item_dict

for item in materials_data:
  item_dict = {}
  item_dict[&#x27;url&#x27;] = item.split(&#x27;~&#x27;)[2]
  item_dict[&#x27;name&#x27;] = list(set(get_tokens(item.split(&#x27;~&#x27;)[0])))
  item_dict[&#x27;real_name&#x27;] = item.split(&#x27;~&#x27;)[0]
  item_dict[&#x27;opis&#x27;] = list(set(get_tokens(materials_data[item])))
  item_dict[&#x27;categ&#x27;] = materials_data[item].split(&#x27;\n&#x27;)[0]
  materials_dict[item.split(&#x27;~&#x27;)[1]] = item_dict</code></pre><p id="5ba164d5-aed7-454d-ac1f-3a983fe82551" class="">Теперь у нас есть два набора тегов для каждого товара: теги из названия и теги из описания.</p><p id="8f151c56-6d03-4f9a-9ec3-2bfd3c818c4d" class="">Осталось перебрать все услуги для всех товаров, все товары для всех услуг и посчитать метрику, по которой будем сортировать рекомендуемые товары и услуги:</p><pre id="b77ee2b3-cbad-4098-9599-bd046e3f5835" class="code"><code>#посчитаем подходящие материалы для каждой услуги, запишем результат в файл
answer = dict()

for usluga in stroyka_dict:
  answer[usluga] = []
  for material in materials_dict:
    intersection_opis = set(stroyka_dict[usluga][&#x27;opis&#x27;])&amp;set(materials_dict[material][&#x27;opis&#x27;])
    intersection_title = set(stroyka_dict[usluga][&#x27;opis&#x27;])&amp;set(materials_dict[material][&#x27;name&#x27;])
    if len(materials_dict[material][&#x27;opis&#x27;]) and len(stroyka_dict[usluga][&#x27;opis&#x27;]): #проверка на zero division
        try:
          if not (materials_dict[material][&#x27;categ&#x27;] in uslugi_towar[stroyka_dict[usluga][&#x27;categ&#x27;]]):
            continue
        except Exception as e:
          continue
        answer[usluga].append({material: len(intersection_opis)/((len(materials_dict[material][&#x27;opis&#x27;])+len(stroyka_dict[usluga][&#x27;opis&#x27;])))+ \ 
					2*len(intersection_title)/(len(stroyka_dict[usluga][&#x27;opis&#x27;]))})
  answer[usluga] = sorted(answer[usluga], key=lambda x: list(x.values())[0], reverse=True)
  answer_with_words = dict()
  for title in answer:
    buffer = []
    for i in range(min(5, len(answer[title]))):
      buffer.append([materials_dict[list(answer[title][i].keys())[0]][&#x27;real_name&#x27;], materials_dict[list(answer[title][i].keys())[0]][&#x27;url&#x27;]])
    answer_with_words[stroyka_dict[title][&#x27;real_name&#x27;]+&#x27;~~&#x27;+stroyka_dict[title][&#x27;url&#x27;]] = buffer

#записываем
with open(&#x27;/content/uslugi_to_materials.json&#x27;, &#x27;w&#x27;, encoding=&#x27;utf-8&#x27;) as fp:
    json.dump(answer_with_words, fp, ensure_ascii=False)</code></pre><p id="58e853c7-b7fe-4673-b6fe-5a611337bf14" class=""> </p><pre id="377276e5-fd03-4eb6-8d07-9a24919e635f" class="code"><code>#теперь выбираем услуги для каждого материала
answer = dict()
all_probs = set()
for material in materials_dict:
  answer[material] = []
  for usluga in stroyka_dict:
    intersection_opis = set(stroyka_dict[usluga][&#x27;opis&#x27;])&amp;set(materials_dict[material][&#x27;opis&#x27;])
    intersection_title = set(stroyka_dict[usluga][&#x27;name&#x27;])&amp;set(materials_dict[material][&#x27;opis&#x27;])
    try:
      if len(materials_dict[material][&#x27;opis&#x27;]) and len(stroyka_dict[usluga][&#x27;opis&#x27;]):
        try:
          if not (stroyka_dict[usluga][&#x27;categ&#x27;] in towar_uslugi[materials_dict[material][&#x27;categ&#x27;]]):
            continue
        except Exception as e:
          all_probs.add(materials_dict[material][&#x27;categ&#x27;])
          continue
        answer[material].append({usluga: len(intersection_opis)/((len(materials_dict[material][&#x27;opis&#x27;])+len(stroyka_dict[usluga][&#x27;opis&#x27;])))+2*len(intersection_title)/(len(materials_dict[material][&#x27;opis&#x27;]))})
    except Exception as e:
      continue
  answer[material] = sorted(answer[material], key=lambda x: list(x.values())[0], reverse=True)
  answer_with_words = dict()
  for title in answer:
    buffer = []
    for i in range(min(5, len(answer[title]))):
      buffer.append([stroyka_dict[list(answer[title][i].keys())[0]][&#x27;real_name&#x27;], stroyka_dict[list(answer[title][i].keys())[0]][&#x27;url&#x27;]])
    answer_with_words[materials_dict[title][&#x27;real_name&#x27;]+&#x27;~~&#x27;+materials_dict[title][&#x27;url&#x27;]] = buffer

with open(&#x27;/content/materials_to_uslugi.json&#x27;, &#x27;w&#x27;, encoding=&#x27;utf-8&#x27;) as fp:
    json.dump(answer_with_words, fp, ensure_ascii=False)</code></pre><p id="6d766286-7773-49b4-807c-cf9c1c1dfba8" class="">Пересечение описания услуги и названия товара более ценно, что отражено в формуле ниже:</p><figure id="e8ec6360-9a3e-43c9-95b3-86e050cdb166" class="equation"><style>@import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.13.2/katex.min.css')</style><div class="equation-container"><span class="katex-display"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow><mi>v</mi><mi>a</mi><mi>l</mi><mo>=</mo><mfrac><mrow><mi>i</mi><mi>n</mi><mi>t</mi><mi>e</mi><mi>r</mi><mi>s</mi><mi>e</mi><mi>c</mi><mi mathvariant="normal">_</mi><mi>d</mi><mi>e</mi><mi>s</mi><mi>c</mi><mi>r</mi><mi>i</mi><mi>p</mi><mi>t</mi></mrow><mrow><mi>d</mi><mi>e</mi><mi>s</mi><mi>c</mi><mi>r</mi><mi>i</mi><mi>p</mi><mi>t</mi><mi mathvariant="normal">_</mi><mi>o</mi><mi>v</mi><mi>e</mi><mi>r</mi><mi>a</mi><mi>l</mi><mi>l</mi><mi mathvariant="normal">_</mi><mi>s</mi><mi>i</mi><mi>z</mi><mi>e</mi></mrow></mfrac><mo>+</mo><mn>2</mn><mo>⋅</mo><mfrac><mrow><mi>i</mi><mi>n</mi><mi>t</mi><mi>e</mi><mi>r</mi><mi>s</mi><mi>e</mi><mi>c</mi><mi mathvariant="normal">_</mi><mi>t</mi><mi>i</mi><mi>t</mi><mi>l</mi><mi>e</mi></mrow><mrow><mi>t</mi><mi>a</mi><mi>r</mi><mi>g</mi><mi>e</mi><mi>t</mi><mi mathvariant="normal">_</mi><mi>d</mi><mi>e</mi><mi>s</mi><mi>c</mi><mi>r</mi><mi>i</mi><mi>p</mi><mi>t</mi></mrow></mfrac></mrow><annotation encoding="application/x-tex">val=\frac{intersec\_ descript}{descript\_overall\_size}+2\cdot\frac{intersec\_ title}{target\_descript}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.03588em;">v</span><span class="mord mathnormal">a</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:2.39044em;vertical-align:-0.996em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.39444em;"><span style="top:-2.314em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathnormal">d</span><span class="mord mathnormal" style="margin-right:0.02778em;">escr</span><span class="mord mathnormal">i</span><span class="mord mathnormal">pt</span><span class="mord" style="margin-right:0.02778em;">_</span><span class="mord mathnormal">o</span><span class="mord mathnormal" style="margin-right:0.03588em;">v</span><span class="mord mathnormal" style="margin-right:0.02778em;">er</span><span class="mord mathnormal">a</span><span class="mord mathnormal" style="margin-right:0.01968em;">ll</span><span class="mord" style="margin-right:0.02778em;">_</span><span class="mord mathnormal">s</span><span class="mord mathnormal">i</span><span class="mord mathnormal">ze</span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.6999999999999997em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathnormal">in</span><span class="mord mathnormal">t</span><span class="mord mathnormal">ersec</span><span class="mord" style="margin-right:0.02778em;">_</span><span class="mord mathnormal">d</span><span class="mord mathnormal" style="margin-right:0.02778em;">escr</span><span class="mord mathnormal">i</span><span class="mord mathnormal">pt</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.996em;"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:0.64444em;vertical-align:0em;"></span><span class="mord">2</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">⋅</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:2.39044em;vertical-align:-0.996em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.39444em;"><span style="top:-2.314em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathnormal">t</span><span class="mord mathnormal">a</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal" style="margin-right:0.03588em;">g</span><span class="mord mathnormal">e</span><span class="mord mathnormal">t</span><span class="mord" style="margin-right:0.02778em;">_</span><span class="mord mathnormal">d</span><span class="mord mathnormal" style="margin-right:0.02778em;">escr</span><span class="mord mathnormal">i</span><span class="mord mathnormal">pt</span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.6999999999999997em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathnormal">in</span><span class="mord mathnormal">t</span><span class="mord mathnormal">ersec</span><span class="mord" style="margin-right:0.02778em;">_</span><span class="mord mathnormal">t</span><span class="mord mathnormal">i</span><span class="mord mathnormal" style="margin-right:0.01968em;">tl</span><span class="mord mathnormal">e</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.996em;"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></span></div></figure><p id="684bf822-5574-4c92-a580-8efe0b021449" class="">Используется мера TF-IDF, то есть количество “попаданий” тегов делится на их общее количество. В первом слагаемом это суммарный размер описаний услуги и товара, во втором - размер описания карточки, для которой мы рекомендуем.</p><p id="7b2bbcb1-722e-4329-97df-3060f44af3ab" class="">
</p><p id="705165bc-1470-427c-9ce3-05db20537160" class="">Помимо всего прочего важно отсеять теги, которые встречаются часто, но важную информацию не несут:</p><pre id="02cffa6c-2599-49ab-a60c-73e5f4dc7950" class="code"><code>stop_words = dict()
all_tags_to_freq = dict()
for material in stroyka_dict:
  for tag in stroyka_dict[material][&#x27;name&#x27;]:
    if tag in all_tags_to_freq:
      all_tags_to_freq[tag] += 1
    else:
      all_tags_to_freq[tag] = 1
  for tag in stroyka_dict[material][&#x27;opis&#x27;]:
    if tag in all_tags_to_freq:
      all_tags_to_freq[tag] += 1
    else:
      all_tags_to_freq[tag] = 1

all_tags = sorted(all_tags_to_freq, key=lambda x: all_tags_to_freq[x], reverse=True)
for i in all_tags:
  print(i, all_tags_to_freq[i])</code></pre><p id="59fa62db-ec00-404b-9ea0-2cd7cd350b41" class="">В результате получен набор слов <a href="https://github.com/MeganJard/RSHB_Project_Bogdanov_Jaroslav/blob/main/custom_stopwords.txt">custom_stopwords.txt</a></p><p id="9d2a7fc0-df72-42f4-af51-da30a74d5dc4" class="">
</p><h2 id="a845d12b-abac-450e-9098-60463e36c49b" class="">Шаг 4. Анализ результатов</h2><p id="3a292ddb-dcad-4a7b-ae6a-ccf51615a338" class="">Итого были получены два json-файла: </p><p id="771ffedd-6d27-4e00-b0b3-e156ca82240e" class=""><a href="https://github.com/MeganJard/RSHB_Project_Bogdanov_Jaroslav/blob/main/uslugi_to_materials%20(2).json">uslugi_to_materials.json</a>:</p><pre id="b5f0bf87-1bd5-4489-ad9e-4b8a93389d10" class="code"><code>{
	&quot;Облицовка ступеней керамической плиткой~~https://svoe-selo.ru/services-catalog/oblicovka-stupenej-keramicheskoj-plitkoj&quot;: [
    [
      &quot;Керамическая плитка&quot;,
      &quot;https://svoe-selo.ru/services-catalog/-internet-magazin-keramicheskoj-plitki&quot;
    ],
    [
      &quot;Плитка&quot;,
      &quot;https://svoe-selo.ru/services-catalog/plitka&quot;
    ],
    [
      &quot;Тротуарная плитка&quot;,
      &quot;https://svoe-selo.ru/services-catalog/trotuarnaya-plitka-4&quot;
    ]
  ],
&quot;Шпатлевка откосов шириной до 400 мм~~https://svoe-selo.ru/services-catalog/shpatlevka-otkosov-shirinoj-do-400-mm&quot;: [
    [
      &quot;Товары для отделки стен&quot;,
      &quot;https://svoe-selo.ru/services-catalog/tovary-dlya-otdelki-sten&quot;
    ],
    [
      &quot;Торговля стройматериалами для внутренней отделки&quot;,
      &quot;https://svoe-selo.ru/services-catalog/torgovlya-strojmaterialami-dlya-vnutrennej-otdelki-1&quot;
    ],
    [
      &quot;Торговля стройматериалами для внутренней отделки&quot;,
      &quot;https://svoe-selo.ru/services-catalog/torgovlya-strojmaterialami-dlya-vnutrennej-otdelki&quot;
    ],
    [
      &quot;Материалы внутренней отделки&quot;,
      &quot;https://svoe-selo.ru/services-catalog/materialy-dlya-vnutrennej-obdelki-&quot;
    ],
    [
      &quot;Материалы для внутренней отделки&quot;,
      &quot;https://svoe-selo.ru/services-catalog/materialy-dlya-vnutrennej-otdelki&quot;
    ]
...
}</code></pre><p id="70475d87-7400-4e5d-99d9-f4ecafc871a8" class="">
</p><p id="c6e6b830-a731-407b-958f-b1f8b3f534fa" class=""><a href="https://github.com/MeganJard/RSHB_Project_Bogdanov_Jaroslav/blob/main/materials_to_uslugi%20(2).json">uslugi_to_materials.json</a>:</p><pre id="4dbb7336-3f89-447d-a6d8-75c20d751bc2" class="code"><code>{
  &quot;Окна ПВХ~~https://svoe-selo.ru/services-catalog/okna-pvx-3&quot;: [
    [
      &quot;Пластиковые окна&quot;,
      &quot;https://svoe-selo.ru/services-catalog/plastikovye-okna--1&quot;
    ],
    [
      &quot;Установка окон&quot;,
      &quot;https://svoe-selo.ru/services-catalog/ustanovka-okon-14&quot;
    ],
    [
      &quot;Установка окон&quot;,
      &quot;https://svoe-selo.ru/services-catalog/ustanovka-okon-20&quot;
    ],
    [
      &quot;Установка и продажа окон&quot;,
      &quot;https://svoe-selo.ru/services-catalog/ustanovka-i-prodazha-okon&quot;
    ],
    [
      &quot;Установка окон&quot;,
      &quot;https://svoe-selo.ru/services-catalog/ustanovka-okon-33&quot;
    ]
  ],
&quot;Утеплитель~~https://svoe-selo.ru/services-catalog/uteplitel-1&quot;: [
    [
      &quot;Наружная отделка жилого дома&quot;,
      &quot;https://svoe-selo.ru/services-catalog/naruzhnaya-otdelka-zhilogo-doma&quot;
    ],
    [
      &quot;Отделка фасада&quot;,
      &quot;https://svoe-selo.ru/services-catalog/otdelka-fasada&quot;
    ],
    [
      &quot;Монтаж и отделка фасада&quot;,
      &quot;https://svoe-selo.ru/services-catalog/montazh-i-otdelka-fasada&quot;
    ],
    [
      &quot;Внешняя отделка домов&quot;,
      &quot;https://svoe-selo.ru/services-catalog/vneshnyaya-otdelka-domov&quot;
    ],
    [
      &quot;Отделка фасада частного дома&quot;,
      &quot;https://svoe-selo.ru/services-catalog/otdelka-fasada-chastnogo-doma&quot;
    ]
  ],
...
}</code></pre><p id="f11842b0-c192-41c3-be21-4c3ae54de5d9" class="">Наилучшего результата можно достигнуть, если:</p><p id="106ecb53-3f78-4d4e-81ae-85754e71fa97" class="">1) Cделать подробное описание для всех услуг и товаров. Указать в описании товара услуги, для которых он необходим и наоборот. Также в идеале описание всех товаров и услуг должно быть примерно одного размера, чтобы формула подсчета работала нормально</p><p id="88cdf3c0-0fd7-443c-a814-c3b2b0f02b9c" class="">2) Исправить определенные неточности в категориях магазина (некоторые товары и услуги в категориях имеют не подкатегории, а категории или даже надкатегории, что мешает нормальной работе алгоритма) </p><p id="929042ea-dcd0-430a-aeaa-54e972d27095" class="">3) Опционально изменить таблицу соответствия категорий товаров и услуг, если необходимо</p><p id="bd44c75e-0724-4169-8b6e-3fd2f982ac0f" class="">4) Повторить всю вышеописаннную цепочку действий(запустить парсер и выполнить пошагово все действия в jupyter-notebook)</p><p id="cf29ed6e-3718-4d56-b12f-0d6dc9d4b991" class="">5) Использовать сервисы для оценки посещаемости и анализа поведения пользователя(Яндекс.Метрика, Google Analytics и.т.д)</p></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>
