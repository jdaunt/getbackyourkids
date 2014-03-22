<!DOCTYPE html>

<html>
<head>
	<meta charset="utf-8">
	<title>Get Back Your Kids</title>
	<link rel="stylesheet" href="../css/style.css">	
</head>

<?php
//Get post variables
$contact_name = htmlspecialchars($_POST["name"]);
$contact_email = htmlspecialchars($_POST["email"]);


// Create connection
$con=mysqli_connect('gbykuser.db.12389615.hostedresource.com', 'gbykuser', 'DMNInc88!', 'gbykuser');

// Check connection
if (mysqli_connect_errno()) {
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
else {
	mysqli_query($con,"UPDATE Counters SET Page1Submit = Page1Submit + 1");
	if (strlen($contact_name) > 0 or strlen($contact_email) > 0) {
		if (strlen($contact_name) == 0) {
			$contact_name = "NA";
		}
		if (strlen($contact_email) == 0) {
			$contact_email = "NA";
		}
		mysqli_query($con,"INSERT INTO Contacts (Name, Email) VALUES ('$contact_name', '$contact_email')");
	}
	mysqli_close($con);
	}
?>

<body>
	<div id="outer">
		<p id="linkcenter"><iframe src="http://www.youtube.com/embed/Iitp5Xh6bMM" name="iframe_a" height="200"></iframe></p>
		<h1><a href="http://www.youtube.com/embed/Iitp5Xh6bMM" target="iframe_a">Bonus Video</a></h1>
		<div id="commentform">	
			<form action="gbykcomments.php" method="post">
				<h2> Comments </h2>
				<h3><label for="name">  Name: </label><input name="name" id="name" maxlength="50" required value=
<?php
$contact_name = htmlspecialchars($_POST["name"]);
echo "$contact_name"
?>
><br>
				<label for="email">  Email: </label> <input name="email" type="email" id="email" maxlength="50" value=
<?php
$contact_email = htmlspecialchars($_POST["email"]);
echo "$contact_email"
?>
><br>
				<textarea rows="10" cols="40" value="comment" name="message" id="message" maxlength="2000" required></textarea>
				</h3>
				<h1><input type="submit" value="  Submit  " style="font-size:20px"></h1>
			</form>
		</div><p></p></div>	
</body>

</html>
