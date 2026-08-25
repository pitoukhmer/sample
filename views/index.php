<div class="sample-container">

	<header class="sample-header">
		<h1 class="sample-header__title">{{ helper:lang line="sample:items" }}</h1>
	</header>

	{{ if items_exist == false }}

		<div class="sample-empty">
			<p class="sample-empty__title">{{ helper:lang line="sample:no_items" }}</p>
			<p class="sample-empty__hint">{{ helper:lang line="sample:no_items_hint" }}</p>
		</div>

	{{ else }}

		<div class="sample-data">
			<table class="sample-data__table">
				<caption class="sample-data__caption">{{ helper:lang line="sample:item_list" }}</caption>
				<thead class="sample-data__thead">
					<tr>
						<th class="sample-data__th" scope="col">{{ helper:lang line="sample:name" }}</th>
						<th class="sample-data__th" scope="col">{{ helper:lang line="sample:slug" }}</th>
					</tr>
				</thead>
				<tbody class="sample-data__tbody">
					<!-- Here we loop through the $items array -->
					{{ items }}
					<tr class="sample-data__row">
						<td class="sample-data__td sample-data__name">
							<span class="sample-data__label">{{ helper:lang line="sample:name" }}</span>
							{{ name }}
						</td>
						<td class="sample-data__td sample-data__slug">
							<span class="sample-data__label">{{ helper:lang line="sample:slug" }}</span>
							{{ slug }}
						</td>
					</tr>
					{{ /items }}
				</tbody>
			</table>
		</div>

		<nav class="sample-pagination" aria-label="{{ helper:lang line="sample:items" }}">
			{{ pagination:links }}
		</nav>

	{{ endif }}

</div>
