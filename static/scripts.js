async function sendMessage(){

const input=document.getElementById("message");

const text=input.value.trim();

if(text==="") return;

const chat=document.getElementById("chat-box");

chat.innerHTML+=`<div class="user-message">${text}</div>`;

input.value="";

chat.innerHTML+=`<div class="bot-message" id="loading">🤖 Thinking...</div>`;

chat.scrollTop=chat.scrollHeight;

const response=await fetch("/chat",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

message:text

})

});

const data=await response.json();

document.getElementById("loading").remove();

chat.innerHTML+=`<div class="bot-message">${data.reply}</div>`;

chat.scrollTop=chat.scrollHeight;

}

document.getElementById("message").addEventListener("keypress",function(e){

if(e.key==="Enter"){

sendMessage();

}

});

function startVoice(){

if(!('webkitSpeechRecognition' in window)){

alert("Speech Recognition is not supported in this browser.");

return;

}

const recognition=new webkitSpeechRecognition();

recognition.lang="en-US";

recognition.interimResults=false;

recognition.maxAlternatives=1;

recognition.start();

recognition.onresult=function(event){

const text=event.results[0][0].transcript;

document.getElementById("message").value=text;

sendMessage();

};

recognition.onerror=function(){

alert("Could not recognize voice.");

};

}