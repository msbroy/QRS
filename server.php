<?php
include 'myfile.txt';
$file = file_get_contents('myfile.txt');
echo $file;

$fopen = fopen($file,"r");    
$data = fgetcsv($fopen, 1000, ",");
fclose($fopen);

?>
