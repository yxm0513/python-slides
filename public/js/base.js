(function() {
    window.changeBackgroundColor = cls => {
        //const classList = wsInstance.currentSlide_.el.classList;
        //classList.forEach(a => {
        //    if (/^bg-/.test(a)) {
        //        classList.remove(a);
        //    }
        //});
        //classList.add(cls);
    };
})();

document.addEventListener("DOMContentLoaded", function(event) {
	changeBackgroundColor('bg-apple')
});
