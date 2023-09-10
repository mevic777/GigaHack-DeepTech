let questionInput = document.querySelector(".input-bar");
let convoBox = document.querySelector(".conversation");
let userQuestion;
let sendMessageButton = document.querySelector(".sendMessageBtn");

const answerOutput = "{{ reply }}";

const sendUserMessage = (message, lineName, className) => {
	const chatLine = document.createElement("li");
	chatLine.classList.add(lineName, className);
	let chatContent = className === "question-text" ? `<p></p>` : ``;
	chatLine.innerHTML = chatContent;
	chatLine.querySelector("p").textContent = message;
	return chatLine;
};

const handleChat = () => {
	userQuestion = questionInput.value.trim();
	if (!userQuestion) return;
	convoBox.appendChild(
		sendUserMessage(userQuestion, "question", "question-text")
	);
	questionInput.value = "";
	convoBox.scrollTo(0, convoBox.scrollHeight);
};

sendMessageButton.addEventListener("click", handleChat);
document.body.addEventListener("keydown", (ev) => {
	if (ev.key === "Enter") handleChat();
	const answerLine = document.createElement("li");
	answerLine.classList.add(lineName, className);
	let chatContent = className === "question-text" ? `<p></p>` : ``;
	answerLine.innerHTML = chatContent;
});
