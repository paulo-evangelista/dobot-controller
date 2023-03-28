extends Control

# Called when the node enters the scene tree for the first time.
func _ready():
	pass

func _on_atualizar_pressed():
	var http_request = HTTPRequest.new()
	add_child(http_request)
	http_request.request_completed.connect(self._http_request_completed)
	var error = http_request.request("http://127.0.0.1:3000/getLastPositions")
	if error != OK:
		push_error("An error occurred in the HTTP request.")

# Called when the HTTP request is completed.
func _http_request_completed(result, response_code, headers, body):
	var json = JSON.new()
	json.parse(body.get_string_from_utf8())
	var response = json.get_data()
	print(response)

		#junta1
	$MarginContainer/HBoxContainer/PanelContainer/VBoxContainer3/Junta1container/ProgressBar.value=response[0]["j1"]
		#junta2
	$MarginContainer/HBoxContainer/PanelContainer/VBoxContainer3/Junta2container/ProgressBar.value=response[0]["j2"]
		#junta3
	$MarginContainer/HBoxContainer/PanelContainer/VBoxContainer3/junta3container/ProgressBar.value=response[0]["j3"]

		#ultima junta1#
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar1.value=response[1]["j1"]
		#ultima junta2
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar2.value=response[1]["j2"]
		#ultima junta3
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar3.value=response[1]["j3"]
	
		#penultima junta1
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar4.value=response[2]["j1"]
		#penultima junta2
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar5.value=response[2]["j2"]
		#penultima junta3
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar6.value=response[2]["j3"]



