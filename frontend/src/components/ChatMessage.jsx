// src/components/ChatMessage.jsx
const ChatMessage = ({ message }) => {
	const isUser = message.role === 'user';
	const isError = message.role === 'error';

	return (
	  <div
		className={`
		  p-4 rounded-lg max-w-[80%]
		  ${isUser
			? 'ml-auto bg-blue-100 text-blue-900'
			: isError
			  ? 'bg-red-100 text-red-900'
			  : 'bg-gray-100 text-gray-900'
		  }
		`}
	  >
		<p className="text-sm font-semibold mb-1">
		  {isUser ? 'Sen' : isError ? 'Hata' : 'AI Asistan'}
		</p>
		<p className="text-gray-700 whitespace-pre-wrap">{message.content}</p>
	  </div>
	);
  };

  export default ChatMessage;
