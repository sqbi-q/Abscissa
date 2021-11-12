const theme_articles = document.querySelectorAll(".theme_article");

function showThemeArticle(target_id) {

    theme_articles.forEach(function(article) {
        article.style.opacity = "0.0";
        article.style.display = "none";
    });

    let target = document.getElementById(target_id);
    target.style.display = "block";
    target.style.opacity = "1.0";
}


const showMoreDesc_elem = document.getElementById("show_more_desc");

function showMore() {
    showMoreDesc_elem.style.display = "block";
}





document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', function (e) {
        e.preventDefault();
        var href = this.getAttribute("href");
        var elem = document.querySelector(href)||document.querySelector("a[name="+href.substring(1, href.length)+"]");
        document.body.scroll({
            top: elem.offsetTop, 
            left: 0, 
            behavior: 'smooth' 
        });
    });
});