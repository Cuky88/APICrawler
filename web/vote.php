<?php 

extract( $_POST, EXTR_OVERWRITE );

$servername = "localhost";
$username = "webapi";
$password = "kdd2017";
$dbname = "webapi";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
	die("Connection failed: " . $conn->connect_error);
}

if($bool && $bool!="false") {
	$sql = "INSERT INTO votes SET No=No, id=" . $conn->real_escape_string($id) . ", name='" . $conn->real_escape_string($name) . "' , cluster_id='" . $conn->real_escape_string($cluster_id) . "', Yes=1 ON DUPLICATE KEY UPDATE Yes=Yes+1";
} else {
	$sql = "INSERT INTO votes SET Yes=Yes, id=" . $conn->real_escape_string($id) .  ", name='" . $conn->real_escape_string($name) . "', cluster_id='" . $conn->real_escape_string($cluster_id) . "', No=1 ON DUPLICATE KEY UPDATE No=No+1";	
}

if ($conn->query($sql) === TRUE) {
	echo "Record updated successfully";
} else {
	echo "Error updating record: " . $conn->error;
}

$conn->close();




?>