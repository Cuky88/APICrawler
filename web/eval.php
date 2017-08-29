<!--  Adapted from https://jqueryui.com/autocomplete/#custom-data 
 Non case sensitive autosearch from https://stackoverflow.com/questions/11237394/jquery-autocomplete-case-sensitive-for-utf-8-characters -->
<!doctype html>
<html>
	<head>
		<title>Webapi Clustering</title>
		<style>
		
		 td, th {
		 
		  border:1px solid #1D0C53;
		  padding:5px;
		 
		 }
		 
		 
		
		</style>
	</head>
	<body>
		<p> --- Work in progress --- </p>
		<h1>Webapi Clustering - Evaluation</h1>
		<p>Here are some statistics about the users votes whether the clustering was useful for them or not.
		</p>
		<table>
			<tr>
				<th>Sum yes</th>
				<th>Sum no</th>
				<th>Avg yes</th>
				<th>Avg no</th>
				<th>Var yes</th>
				<th>Var no</th>
				<th>Total number of votes</th>
			</tr>
            <?php 
            
            /*Code parts taken from https://www.w3schools.com/php/php_mysql_select.asp
             * 
             * 
             */
            
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
            
            $sql = "SELECT SUM(yes) as yesSum, 
                        SUM(no) as noSum, 
                        AVG(yes) as yesAvg, 
                        AVG(no) as noAvg, 
                        VARIANCE(yes) as yesVar, 
                        VARIANCE(no) as noVar, 
                        (SUM(yes) / (SUM(yes) + SUM(no))) as quality,  
                        COUNT(id), (SUM(yes)+SUM(no)) as numVotes 
                    FROM votes";
            $result = $conn->query($sql);
            
            if ($result->num_rows > 0) {
                // output data of each row
                while($row = $result->fetch_assoc()) {
                    echo '<tr>
                        <td>' . $row['yesSum'] . '</td>
                        <td>'  . $row['noSum'] . '</td>
                        <td>'  . $row['yesAvg'] . '</td>
                        <td>'  . $row['noAvg'] . '</td>
                        <td>'  . $row['yesVar'] . '</td>
                        <td>'  . $row['noVar'] . '</td>
                        <td>'  . $row['numVotes'] . '</td>
                    </tr></table>
                    <p>We reached a <b>quality of ' . $row['quality'] . '</b> by ' . $row['numVotes'] . ' given votes.</p>';
                }
            } else {
                echo "0 results";
            }
            $conn->close();
            
            
            
            ?>
		
		<br><br><br><br>
		<footer style="font-size:12px">Impressum: Jan-Peter Schmidt, Lilienweg 5a, 74847 Obrigheim</footer>
	</body>
</html>