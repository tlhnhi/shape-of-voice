var mice = document.getElementById('mice');
var camera = document.getElementById('camera');
var share = document.getElementById('share');

mice.addEventListener('click', (mice) => {
	mice.target.classList.toggle('mice-on');
	console.log(mice.target.classList);
});

camera.addEventListener('click', (camera) => {
	camera.target.classList.toggle('camera-on');
});

share.addEventListener('click', (share) => {
	share.target.classList.toggle('share-on');
})