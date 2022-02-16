import './App.css';
import React from 'react';
//import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

const API_HOST = "http://localhost";

function App() {
	function generateShortenedURL() {
		var url = document.getElementById("input_url").value;
		
		const requestOptions = {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({"url": url})
		};
		
		fetch(`${API_HOST}/api/shorten`, requestOptions)
			.then(response => response.json())
			.then(data => {
				var label = document.getElementById("message");
				
				if (data.success) {
					label.textContent = "The generated URL link is " + data.generated_url;
				} else {
					label.textContent = "Invalid URL";
				}
			});
	}
	
	return (
		<div className="App">
			<div>
				<h1 align="center">URL Shortener Service</h1>
				
				<table align="center">
					<tbody>
						<tr>
							<td align="left" width="400" colSpan="2" >
								Enter the URL link that you would like to shorten:
							</td>
						</tr>
						<tr>
							<td align="left" width="200">
								<input id="input_url" type="text"/>
							</td>
							<td align="left" width="200">
								<button onClick={() => generateShortenedURL()}>
									Shorten
								</button>
							</td>
						</tr>
						<tr>
							<td align="left" width="400" colSpan="2">
								<label id="message"/>
							</td>
						</tr>
					</tbody>
				</table>
			</div>
		</div>
	);
}

export default App;