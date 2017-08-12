coucou<?php

/*

Congratz!

Le mot de passe de validation est : 
The validation password is : 

R3m0t3_iS_r3aL1y_3v1l

*/

$language="en";
if ( isset($_GET["lang"]) ){
    $language = $_GET["lang"];
}
include($language."_lang.php");
?>

<html>
<head><title>Remote File Inclusion</title></head>

<body>

<h3>
    <?php echo $lang['lang']; ?> : 
    <a href="?lang=fr" style="text-decoration:<?php ($language=="fr")?print "underline":print "none"; ?>">Français</a>
    &nbsp;|&nbsp;
    <a href="?lang=en" style="text-decoration:<?php ($language=="en")?print "underline":print "none"; ?>">English</a>
</h3>

<p><?php echo $lang["welcome"]; ?></p>

</body>
</html>
