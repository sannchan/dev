<?php
	include(dirname(__FILE__) . '/module/resorce.php');
	foreach ($res_title as $key => $value) {
		if(strpos($_SERVER["REQUEST_URI"],$key) !== false){
			$param = $value;
			$htag = "p";
		}
		if(empty($param)){
			$param = $res_title["top"];
			$htag = "h1";
		}
	}
?>

<!DOCTYPE html>
<html lang="ja">
<head>
	<meta charset="UTF-8">
	<title><?php echo $param["title"]; ?></title>
	<meta name="discription" content="<?php echo $param["disc"]; ?>">
	<meta name="format-detection" content="telephone=no">
	<meta name="viewport" content="width=device-width">
	<link rel="stylesheet" href="/css/add.css">
	<link rel="stylesheet" href="/css/reset.css">
	<link rel="stylesheet" href="/css/lightbox.css">
	<link rel="stylesheet" href="/css/style.css">
	<link rel="stylesheet" href="/css/style2.css">
	<?php if($param["menu"] == "realestate"){ ?>
	<link rel="stylesheet" href="/css/realestate.css">
	<?php } ?>
	<script src="/js/jquery-3.2.0.min.js" type="text/javascript" charset="utf-8"></script>
	<script src="/js/lightbox.js" type="text/javascript" charset="utf-8"></script>
	<script src="/js/script.js" type="text/javascript" charset="utf-8"></script>
	<script src="/js/jquery.rwdImageMaps.min.js" type="text/javascript" charset="utf-8"></script>
</head>
<body>
	<div id="wrap">
		<header id="global_header">
			<div class="logo">
				<a href="/"><<?php echo $htag; ?>><img src="/img/common/common_header-logo.png" alt="株式会社飛田観光開発"></<?php echo $htag; ?>></a>
			</div>
			<nav>
				<ul>
					<li id="top_header" class="<?php if($param["menu"] == "top"){echo "current";}?> pc-only"><a href="/">　</a></li>
					<li class="<?php if($param["menu"] == "top"){echo "current";}?> sp-only"><a href="/">トップ</a></li>
					<li id="header_2" class="<?php if($param["menu"] == "realestate"){echo "current";}?> pc-only"><a href="/realestate">　</a></li>
					<li class="<?php if($param["menu"] == "realestate"){echo "current";}?> sp-only"><a href="/realestate">不動産物件検索</a></li>
					<li id="header_3" class="<?php if($param["menu"] == "kurihara"){echo "current";}?> pc-only"><a href="/kurihara">　</a></li>
					<li class="<?php if($param["menu"] == "kurihara"){echo "current";}?> sp-only"><a href="/kurihara">かがやきタウン</a></li>
					<li id="header_4" class="<?php if($param["menu"] == "enjoyplaza"){echo "current";}?> pc-only"><a href="/enjoyplaza">　</a></li>
					<li class="<?php if($param["menu"] == "enjoyplaza"){echo "current";}?> sp-only"><a href="/enjoyplaza">エンジョイプラザ</a></li>
					<li id="header_5" class="<?php if($param["menu"] == "kamabutanoyu"){echo "current";}?> pc-only"><a href="/kamabutanoyu"</a>　</li>
					<li class="<?php if($param["menu"] == "kamabutanoyu"){echo "current";}?> sp-only"><a href="/kamabutanoyu">釜ぶたの湯</a></li>
					<li id="header_6" class="<?php if($param["menu"] == "parking"){echo "current";}?> pc-only"><a href="/parking">　</a></li>
					<li class="<?php if($param["menu"] == "parking"){echo "current";}?> sp-only"><a href="/parking">上越妙高駅周辺駐車場</a></li>
					<li id="header_7" class="<?php if($param["menu"] == "contact"){echo "current";}?> pc-only"><a href="/contact">　</a></li>
					<li class="<?php if($param["menu"] == "contact"){echo "current";}?> sp-only"><a href="/contact">お問合せ</a></li>
					<li id="header_8" class="<?php if($param["menu"] == "about"){echo "current";}?> pc-only"><a href="/about">　</a></li>
					<li class="<?php if($param["menu"] == "about"){echo "current";}?> sp-only"><a href="/about">会社概要</a></li>
				</ul>
			</nav>
		</header>
