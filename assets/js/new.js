// 비밀번호와 비밀번호 확인 일치 여부 확인
document.getElementById("join").addEventListener("submit", function(event) {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("passwordConfirm").value;
    if (password != confirmPassword) {
        document.getElementById("pwCheckError").innerHTML = "비밀번호가 일치하지 않습니다.";
        event.preventDefault(); // 폼 제출 방지
    } else {
        document.getElementById("pwCheckError").innerHTML = "";
    }
});

// 이메일 유효성 검사
document.getElementById("email").addEventListener("input", function() {
    var email = this.value;
    var emailError = document.getElementById("emailError");
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)) {
        emailError.innerHTML = "";
    } else {
        emailError.innerHTML = "유효하지 않은 이메일 형식입니다.";
    }
});
