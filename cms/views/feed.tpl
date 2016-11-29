<!doctype html>

<html>
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE-edge">
		<meta name="description" content="Feed of articles for this simple CMS">
		<meta name="viewport" content="width=device-width, initial-scale=1">

		<!-- CSS -->
		<link href="css/main.css" rel="stylesheet">

		<!-- JavaScript -->
		<script src="js/main.js" async></script>

		<title>Feed</title>
	</head>

	<body>
		<h1>This is the feed page!</h1>
		<p>
			<a href="submit">Submit an article</a>
		</p>

		% if not articles:
			<p>There are no articles to display.</p>
		% else:
			% for article in articles:
				<h2>{{article[0]}}</h2>
				<h3>{{article[1]}}</h3>
				<p>{{article[2]}}</p>
			% end
		% end
	</body>
</html>
