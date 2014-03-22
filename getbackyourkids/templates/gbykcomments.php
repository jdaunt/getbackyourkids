<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Get Back Your Kids</title>
	<link rel="stylesheet" href="css/style.css">	
</head>

<?php
//Get post variables
$contact_name = htmlspecialchars($_POST["name"]);
$contact_email = htmlspecialchars($_POST["email"]);
$contact_comment = htmlspecialchars($_POST["message"]);

// Create connection
$con=mysqli_connect('gbykuser.db.12389615.hostedresource.com', 'gbykuser', 'DMNInc88!', 'gbykuser');

// Check connection
if (mysqli_connect_errno()) {
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
else {
	mysqli_query($con,"UPDATE Counters SET Page2Submit = Page2Submit + 1");
	if (strlen($contact_comment) > 0) {
		if (strlen($contact_name) == 0) {
			$contact_name = "NA";
		}
		if (strlen($contact_email) == 0) {
			$contact_email = "NA";
		}
		mysqli_query($con,"INSERT INTO Comments (Name, Email, Comments) VALUES ('$contact_name', '$contact_email', '$contact_comment')");
	}
	mysqli_close($con);
	}
?>

<body>
	<div id="outer">
		<h1>
<?php
$contact_comment = htmlspecialchars($_POST["message"]);
if (strlen($contact_comment) > 0) {
	echo "Thank you for your feedback!";
}
else {
	echo "Hope you enjoyed,";
}
?>
</h1>
	</div>	
</body>
</html>
