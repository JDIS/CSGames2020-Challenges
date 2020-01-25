<?php 
  if(!isset($_COOKIE['debug'])) {
    setcookie('debug', 'false', time() + (86400 * 30), "/");
  } 
?>

<!DOCTYPE html> 
<html>
<head>
  <title>Enrollment</title>
  <link 
    rel="stylesheet" 
    href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" 
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" 
    crossorigin="anonymous">
</head>

<body>
  <h1>Participants</h1>
  <p>Liste des utilisateurs du service csgames.jdis.ca:27777</p>
  <form action="users.php" method="GET">
    <input id="search" name="search" type="text" placeholder="Username here">
    <input id="submit" type="submit" value="Search">
  </form>

  <table>
    <tr>
      <th>Username</th>
      <th>Password</th>
    </tr>

    <?php fetch_users(''); ?>
  </table>
</body>

<?php
  function fetch_users($username){
    $db = new SQLite3('/var/www/db/christmas-chase', SQLITE3_OPEN_CREATE | SQLITE3_OPEN_READWRITE);

    // Create a table.
    $db->query(
    'CREATE TABLE IF NOT EXISTS "users" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        "name" VARCHAR,
        "pwd" VARCHAR
      )'
    );

    $request = 'SELECT * FROM users WHERE name LIKE "' . $_GET['search'] . '%" AND name != "admin"';
    
    if($_COOKIE['debug'] == 'true')
    {
      echo 'flag{Co0ki3$Ftw}<br>';
      echo $request;
    }

    $result = $db->query($request);

    while ($row = $result->fetchArray()) {
      echo '<tr><td>' . $row['name'] . '</td><td>' . $row['pwd'] . '</td></tr>';
    }

    // Close the connection
    $db->close();
  }
  ?>
</html>