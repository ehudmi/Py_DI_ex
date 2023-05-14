// for (let i = 0; i < 6; i++) {}
// console.log(i);

// console.log("hi from after the error");
//here, this log won't go through because it is after the exception
function loop() {
	try {
		for (let i = 0; i < 6; i++) {}
		console.log(i);
	} catch (error) {
		throw new Error("catch in loop function");
	}
	//  finally {
	// console.log("something");
	//finally always happens, whether we catch an error or not.
	// }
}
function x() {
	try {
		loop();
	} catch (error) {
		console.log(error.name, error.message, error.stack);
	}
}
x();
console.log("hi from after the error");
//here, this log will go through, because we are handling the exception. as long as we catch the error, the rest of the code goes through.
