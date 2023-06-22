const User = (props) => {
	const { roboname, email, username, id } = props.info;
	return (
		<div>
			<img src={`https://robohash.org/${id}?size=150x150`} />
			<h2>Name: {roboname}</h2>
			<h4>Email: {email}</h4>
			<p>username: {username}</p>
		</div>
	);
};
export default User;
