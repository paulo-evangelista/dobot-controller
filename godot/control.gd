extends Control

var json = JSON.new()
# Called when the node enters the scene tree for the first time.
func _ready():
	pass
	
func _on_atualizar_pressed():
	$HTTPRequest.request("http://www.mocky.io/v2/5185415ba171ea3a00704eed")


func _on_http_request_request_completed(result, response_code, headers, body):
	var js = json.parse(body.get_string_from_utf8())
	print(js)
	
	
		#junta1
	$MarginContainer/HBoxContainer/PanelContainer/VBoxContainer3/Junta1container/ProgressBar.value=response_code / 6
		#junta2
	$MarginContainer/HBoxContainer/PanelContainer/VBoxContainer3/Junta2container/ProgressBar.value=response_code / 6
		#junta3
	$MarginContainer/HBoxContainer/PanelContainer/VBoxContainer3/junta3container/ProgressBar.value=response_code / 6

		#ultima junta1
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar1.value=response_code / 6
		#ultima junta2
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar2.value=response_code / 6
		#ultima junta3
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar3.value=response_code / 6
	
		#penultima junta1
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar4.value=response_code / 6
		#penultima junta2
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar5.value=response_code / 6
		#penultima junta3
	$MarginContainer/HBoxContainer/PanelContainer2/VBoxContainer/ProgressBar6.value=response_code / 6
	
