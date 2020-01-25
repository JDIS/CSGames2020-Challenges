<?php
    $file = $_GET['page'];
    if(!isset($file))
    {
        header("Location: /?page=home.php");
        die();
    }
    else
    {
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>
    <?php
        include($file);
    ?>
</body>
</html>
<?php
    }
?>