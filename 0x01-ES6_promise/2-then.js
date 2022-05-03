export default function handleResponseFromAPI(promise) {
    return promise.then(
        function(result) {
            console.log('Got a response form the API');
            return {
                status: 200,
                body: 'success',
            }
        },
        function(error) {
            return new Error()
        },
        );
}