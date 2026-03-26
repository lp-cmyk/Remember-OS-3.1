import { useEffect, useState } from "react";

export default function LoginPanel() {
  const [systemPassword, setSystemPassword] = useState("");
  const [inputPwd, setInputPwd] = useState("");
  const [newPwd, setNewPwd] = useState("");

  // 读取配置 JSON
  useEffect(() => {
    async function loadConfig() {
      try {
        let res = await fetch("settings.json");
        let config = await res.json();
        setSystemPassword(config.password);
      } catch (err) {
        console.error("加载配置失败", err);
      }
    }
    loadConfig();
  }, []);

  // 登录验证
  function checkLogin() {
    if (systemPassword === "xxxxxx") {
      alert("登录成功（无密码模式）");
    } else if (inputPwd === systemPassword) {
      alert("登录成功！");
    } else {
      alert("密码错误");
    }
  }

  // 修改密码
  function changePassword() {
    setSystemPassword(newPwd);
    alert("密码已更新：" + newPwd);
  }

  return (
    <div style={{ padding: "20px" }}>
      {/* 登录 */}
      <div>
        <h3>登录</h3>
        密码：
        <input
          type="password"
          value={inputPwd}
          onChange={(e) => setInputPwd(e.target.value)}
        />
        <br />
        <button onClick={checkLogin}>登录</button>
      </div>

      {/* 修改密码 */}
      <div style={{ marginTop: "30px" }}>
        <h3>设置 - 修改密码</h3>
        新密码：
        <input
          value={newPwd}
          onChange={(e) => setNewPwd(e.target.value)}
        />
        <br />
        <button onClick={changePassword}>保存密码</button>
      </div>
    </div>
  );
}