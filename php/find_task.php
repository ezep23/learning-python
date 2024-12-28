<?php 

include("db.php");

$search = $_POST['search'];

if(!empty($search)){
    $query = "SELECT * FROM tasks WHERE name LIKE '$search%'";
    $result = mysqli_query($connection, $query);

    if(!$result){
        die('Error:' . mysqli_error($connection));
    }

    $tasks = array();

    while($row = mysqli_fetch_array($result)){
        $tasks[] = array(
            'name' => $row['name'],
            'description' => $row['description'],
            'id' => $row['id']
        );
    }

    $json_tasks = json_encode($tasks);
    echo $json_tasks;
}