<?php
// displaying as links song title for four (1,2,3,4) icecast streams
// public domain
//
$result = array();
$handle = @fopen("http://some.address.of.icecast.server:8000/status.xsl","r");
if ($handle) {
	$i=0;
	while (($buffer = fgets($handle, 4096)) !== false) {
		        if ($i==68) {
				           $d = preg_split("/<[^>]*[^\/]>/i",$buffer);
					              array_push($result,"<a href=\"http://some.address.of.icecast.server:8000/1.m3u\">".$d[1]."</a>");
					           }
			        else if ($i==126) {
					            $d = preg_split("/<[^>]*[^\/]>/i",$buffer);
						                array_push($result,"<a href=\"http://some.address.of.icecast.server:8000/2.m3u\">".$d[1]."</a>");
						            }
			        else if ($i==184){
					            $d = preg_split("/<[^>]*[^\/]>/i",$buffer);
						                array_push($result,"<a href=\"http://some.address.of.icecast.server:8000/3.m3u\">".$d[1]."</a>");
						            }
			        else if ($i==242) {
					            $d = preg_split("/<[^>]*[^\/]>/i",$buffer);
						                array_push($result,"<a href=\"http://some.address.of.icecast.server:8000/4.m3u\">".$d[1]."</a>");

						            }

			           $i++;
			        }
	fclose($handle);

	foreach ($result as $link) 
		   echo $link."\n";

}
?>  
