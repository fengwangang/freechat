/**
* freechat.js
* author: feng
*/

var uid = 0;
var token = '';
var chat_friend_ID = 0;
var chat_friend_name = '';
var chat_friend_avatar = '';

window.onload = function(){
	initPullMessageEvent();
	bindFriendItemEvent();
	document.getElementById('send_message').onclick=sendMessage;
	document.getElementById('input-message-area').onkeydown=function(event){
		if(13 == event.keyCode){
			sendMessage();
			return false;
		}else{
			return true;
		}
	}
}

function bindFriendItemEvent(){
	var chatPanel = document.getElementById('chatPanel');
	var friendItems = document.getElementsByClassName('friend-list-item');
	for(var i=0,len=friendItems.length;i<len;i++){
		friendItems[i].onclick=function(){
			var friendID = this.getAttribute('friendid');
			var friendName = this.getAttribute('friendname');
			var friendAvatar = this.getAttribute('friendavatar');
			document.getElementById('friendName').innerHTML=friendName;
			chat_friend_ID = friendID;
			chat_friend_name = friendName;
			chat_friend_avatar = friendAvatar;
			chatPanel.style.display='block';
			document.getElementById('input-message-area').focus();
		}
	}
}

function initPullMessageEvent(){
	uid = getCookie('uid');
	token = getCookie('token');
	var requestUrl = '/pull?uid='+uid+'&token='+token;
	$.ajax({
		url: requestUrl,
		type: 'GET',
		dataType: 'json',
		async: true,
		error: function(){
		},
		success: function(data){
			receiveMessage(data);
			pull();
		}
	});
}

function pull(){
	var requestUrl = '/pull?uid='+uid+'&token='+token;
	$.ajax({
		url: requestUrl,
		type: 'GET',
		dataType: 'json',
		async: true,
		error: function(){
		},
		success: function(data){
			receiveMessage(data)
			pull();
		}
	});
}

function sendMessage(){
	var inputMsgArea = document.getElementById('input-message-area');
	if(isEmpty(inputMsgArea.value)){
		return false;
	}
	var sender = uid;
	var receiver = chat_friend_ID;
	var msg_type = 1;
	var msg_content = inputMsgArea.value;
	var time = (new Date()).getTime();
	var messageSendPanel = document.getElementById('message-list-item-send').cloneNode(true);
	messageSendPanel.setAttribute('id',sender+'_'+receiver+'_'+time);
	$(messageSendPanel).find('#message_avatar').attr('src', chat_friend_avatar);
	$(messageSendPanel).find('#message_name').html(chat_friend_name);
	$(messageSendPanel).find('#message_content').html(msg_content);
	messageSendPanel.style.display='block';
	document.getElementById('message_list_area').appendChild(messageSendPanel);
	scrollToBottom();
	inputMsgArea.value='';
	inputMsgArea.focus();
	$.ajax({
		url: '/send',
		type: 'POST',
		dataType: 'json',
		data: {
			sender: sender,
			receiver: receiver,
			msg_type: msg_type,
			msg_content: msg_content
		},
		async: true,
		error: function(){
		},
		success: function(){
			
		}
	});
}

function receiveMessage(message) {
	var sender = message.sender;
	var receiver = message.receiver;
	var msg_type = message.msg_type;
	var content = message.content;
	var time = (new Date()).getTime();
	var messageReceivePanel = document.getElementById('message-list-item-receive').cloneNode(true);
	messageReceivePanel.setAttribute('id',sender+'_'+receiver+'_'+time);
	$(messageReceivePanel).find('#message_avatar').attr('src', chat_friend_avatar);
	$(messageReceivePanel).find('#message_name').html(message.sender);
	$(messageReceivePanel).find('#message_content').html(content);
	messageReceivePanel.style.display='block';
	document.getElementById('message_list_area').appendChild(messageReceivePanel);
	scrollToBottom();
}

/**
 * scroll to bottom 
 */
function scrollToBottom() {
	var messageListArea = document.getElementById('message_list_area');
	var scrollHeight = messageListArea.scrollHeight;
	messageListArea.scrollTop = scrollHeight;
}

function getCookie(c_name){
	if (document.cookie.length > 0){
  		c_start = document.cookie.indexOf(c_name + "=");
  		if (c_start != -1){ 
  			c_start=c_start + c_name.length+1;
    		c_end=document.cookie.indexOf(";",c_start);
    		if (c_end==-1) c_end=document.cookie.length
    			return unescape(document.cookie.substring(c_start,c_end));
    		} 
  		}
	return '';
}

function $ajax(param){
	var ajax = new IAjax(param);
}

function IAjax(param){
	if(undefined == param || null == param){
		return false;
	}
	var request = false;
	try {
		request = new XMLHttpRequest();
	} catch (trymicrosoft) {
		try {
			request = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (othermicrosoft) {
			try {
		        request = new ActiveXObject("Microsoft.XMLHTTP");
		    } catch (failed) {
		        request = false;
		    }  
		}
    }
	if(!request) {
		return false;
	}
	request.open(param.type, param.url, param.async);
	request.onreadystatechange = function(){
	    if(4 == request.readyState) {
	        if(200 == request.status){
	        	param.success(request.data);
	        }else {
	        	param.error(request.data);
	        }
	    }
	}
	request.send();
}

function isEmpty(value){
	if(undefined == value || null == value || '' == value || '' == value.replace(/(^\s*)|(\s*$)/g,'')) {
		return true;
	}
	return false;
}