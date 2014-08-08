/**
* freechat.js
* author: feng
*/

function loginValidate(obj){
	var account = document.getElementById('account');
	if(isEmpty(account.value)){
		document.getElementById('login_error').innerHTML = 'Invalid Account';
		account.focus();
		return false;
	}
	var password = document.getElementById('password');
	if(isEmpty(password.value) || password.value.length<6 || password.value.length>32) {
		document.getElementById('login_error').innerHTML = 'Invalid Password';
		password.focus();
		return false;
	}
	return true;
}

function isEmpty(value){
	if(undefined == value || null == value || '' == value || '' == value.replace(/(^\s*)|(\s*$)/g,'')) {
		return true;
	}
	return false;
}