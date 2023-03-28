extends Control

# Called when the node enters the scene tree for the first time.
func _ready():
	pass
	
func _on_atualizar_pressed():
	$HTTPRequest.request("http://127.0.0.1:3000/getLastPositions")


func _on_HTTPRequest_request_completed( result, response_code, headers, body ):
	#var json2 = JSON.new()
	#var jsone = json2.parse(body.get_string_from_utf8())
	print(headers)
	print(body.size())
	
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
	


