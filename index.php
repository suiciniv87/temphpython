<html>
   <head>
	<meta http-equiv="refresh" content="300">
	<meta charset="UTF-8">
	<title>Informações</title>
	<h1>Dólar, Euro e Temperatura</h1>
   </head>
<?php

$comando = escapeshellcmd('python temp.py');
$cmdResult = shell_exec($comando);
echo $cmdResult;

	

?>
</html>