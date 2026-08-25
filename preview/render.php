<?php
/**
 * Static preview renderer for the Sample module.
 *
 * PyroCMS is not available in CI or in an agent sandbox, so this script renders
 * views/index.php against fixture data and writes plain HTML that a browser --
 * or a headless browser driven by an agent -- can load and verify.
 *
 * It resolves the subset of Lex syntax this view actually uses:
 *   {{ helper:lang line="key" }}          -> language/english/sample_lang.php
 *   {{ if items_exist == false }}..{{ endif }} with optional {{ else }}
 *   {{ items }}..{{ /items }}             -> repeated per fixture row
 *   {{ pagination:links }}                -> fixture pagination markup
 *
 * Usage:  php preview/render.php
 * Output: preview/index.html  (populated)   preview/empty.html  (empty state)
 */

$root = dirname(__DIR__);

// --- language --------------------------------------------------------------
$lang = [];
require $root . '/language/english/sample_lang.php';

// --- fixtures --------------------------------------------------------------
$fixtures = [
    ['name' => 'Getting Started',                 'slug' => 'getting-started'],
    ['name' => 'Module Development Guide',        'slug' => 'module-development-guide'],
    ['name' => 'Working With MY_Model',           'slug' => 'working-with-my-model'],
    ['name' => 'Events, Plugins and Widgets',     'slug' => 'events-plugins-and-widgets'],
    // Deliberately long, to prove the layout does not break on overflow.
    ['name' => 'Migrating A Legacy Theme To The Current Template Engine',
     'slug' => 'migrating-a-legacy-theme-to-the-current-template-engine'],
];

$pagination = <<<'HTML'
<span class="current">1</span>
			<a href="#page-2">2</a>
			<a href="#page-3">3</a>
			<a href="#next">Next &rsaquo;</a>
HTML;

// --- renderer --------------------------------------------------------------

function render(string $template, array $items, array $lang, string $pagination): string
{
    $itemsExist = count($items) > 0;

    // {{ if items_exist == false }} A {{ else }} B {{ endif }}
    $template = preg_replace_callback(
        '/\{\{\s*if\s+items_exist\s*==\s*false\s*\}\}(.*?)(?:\{\{\s*else\s*\}\}(.*?))?\{\{\s*endif\s*\}\}/s',
        static fn (array $m): string => $itemsExist ? ($m[2] ?? '') : $m[1],
        $template
    );

    // {{ items }} row {{ /items }}
    $template = preg_replace_callback(
        '/\{\{\s*items\s*\}\}(.*?)\{\{\s*\/items\s*\}\}/s',
        static function (array $m) use ($items): string {
            $out = '';
            foreach ($items as $item) {
                $row = $m[1];
                foreach ($item as $field => $value) {
                    $row = str_replace('{{ ' . $field . ' }}', htmlspecialchars((string) $value, ENT_QUOTES), $row);
                }
                $out .= $row;
            }
            return $out;
        },
        $template
    );

    // {{ helper:lang line="key" }}
    $template = preg_replace_callback(
        '/\{\{\s*helper:lang\s+line="([^"]+)"\s*\}\}/',
        static fn (array $m): string => htmlspecialchars($lang[$m[1]] ?? $m[1], ENT_QUOTES),
        $template
    );

    // {{ pagination:links }}
    return str_replace('{{ pagination:links }}', $pagination, $template);
}

function page(string $body, string $title): string
{
    return <<<HTML
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{$title} &middot; Sample module preview</title>
<link rel="stylesheet" href="../css/sample.css">
<style>
	/* Preview chrome only -- not part of the module. */
	html, body { margin: 0; padding: 0; background: #fbfbfa; }
	@media (prefers-color-scheme: dark) {
		html:not([data-theme="light"]), html:not([data-theme="light"]) body { background: #141413; }
	}
	html[data-theme="dark"], html[data-theme="dark"] body { background: #141413; }
</style>
</head>
<body>
{$body}
</body>
</html>
HTML;
}

// --- write -----------------------------------------------------------------

$template = file_get_contents($root . '/views/index.php');

file_put_contents(
    $root . '/preview/index.html',
    page(render($template, $fixtures, $lang, $pagination), 'Item list')
);

file_put_contents(
    $root . '/preview/empty.html',
    page(render($template, [], $lang, $pagination), 'Empty state')
);

echo "Rendered preview/index.html (" . count($fixtures) . " rows) and preview/empty.html\n";
