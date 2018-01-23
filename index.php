<?php

$page = $_SERVER['PHP_SELF'];
$sec = "8";
header("Refresh: $sec; url=$page");


$file = 'status.txt';

if (!empty($_GET)) {
    $name = $_GET['name'];
    file_put_contents($file, $name);
}

$filename = "status.txt";
$fp = fopen($filename, "r");

$content = fread($fp, filesize($filename));
fclose($fp);

if($content == "full"){
//do stuff
}
?>
