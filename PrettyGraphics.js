'use strict';
if ( ! Detector.webgl ) Detector.addGetWebGLMessage();

let aspect = window.innerWidth/window.innerHeight;
let container,
	scene,
	camera,
	renderer,
	geometry,
	material,
	cube,
	directionalLight,
	backLight,
	stats;

let onWindowResize = function(){

	camera.aspect = window.innerWidth / window.innerHeight;
	camera.updateProjectionMatrix();
	renderer.setSize( window.innerWidth, window.innerHeight );

}


let render = function() {
	cube.rotation.x += 0.01;
	cube.rotation.y += 0.01;
	cube.rotation.z += 0.005;
	renderer.render(scene, camera);
}

let animate = function(){
	requestAnimationFrame( animate );
	render();
	stats.update();
}

let init = function(){
	container = document.createElement( 'div' );
	container.style.zIndex="-1";
	container.style.position="absolute";
	container.style.x="0px";
	container.style.y="0px";
	document.body.appendChild( container );
	
	scene = new THREE.Scene();
	camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );
	
	// http://threejs.org/docs/#Manual/Introduction/Creating_a_scene

	geometry = new THREE.BoxGeometry( 2.5, 2.5, 2.5 );
	material = new THREE.MeshPhongMaterial( { color: 0xdddddd, specular: 0x009900, shininess: 70, shading: THREE.FlatShading } )
	cube = new THREE.Mesh( geometry, material );
	scene.add( cube );

	directionalLight = new THREE.DirectionalLight( 0xffffff, 0.5 );
	directionalLight.position.set( 0, 1, 0 );
	
	backLight = new THREE.DirectionalLight( 0x444444, 0.5 );
	backLight.position.set( 1, -1, 0.5 );
	
	scene.add( directionalLight );
	scene.add( backLight );

	camera.position.z = 5;

	// http://stackoverflow.com/questions/9899807/three-js-detect-webgl-support-and-fallback-to-regular-canvas


	//renderer =  Detector.webgl ? new THREE.WebGLRenderer({ alpha: true }): new THREE.CanvasRenderer({ alpha: true });
	renderer = new THREE.WebGLRenderer( { alpha: true } );
	renderer.setPixelRatio( window.devicePixelRatio );
	renderer.setSize( window.innerWidth, window.innerHeight );
	renderer.domElement.style.position = "absolute";
	renderer.domElement.style.x = "0px";
	renderer.domElement.style.y = "0px";
	container.appendChild( renderer.domElement );

	stats = new Stats();
	stats.domElement.style.position = 'absolute';
	stats.domElement.style.top = '0px';

	container.appendChild( stats.domElement );
	
	window.addEventListener( 'resize', onWindowResize, false );
}

init();
animate();
