from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common.exceptions import WebDriverException

def login_user(driver, username, password):
    """执行登录操作的通用函数"""
    try:
        # 显式等待输入框加载
        username_field = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.ID, "username"))
        )
        password_field = driver.find_element(By.ID, "password")

        # 清空字段并输入信息
        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)

        # 选择最后一个域名选项
        domain_select = driver.find_element(By.ID, "domain")
        domain_options = domain_select.find_elements(By.TAG_NAME, "option")
        if domain_options:
            domain_options[-1].click()  # 点击最后一个选项

        # 确保记住密码被勾选
        remember_checkbox = driver.find_element(By.ID, "remember")
        if not remember_checkbox.is_selected():
            remember_checkbox.click()

        # 点击登录按钮
        login_button = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.ID, "login-account"))
        )
        login_button.click()

        # 验证登录是否成功
        WebDriverWait(driver, 10).until(
            ec.url_contains("srun_portal_success")
        )
        print(f"账号 {username} 登录成功")

    except (NoSuchElementException, TimeoutException) as e:
        print(f"登录过程中发生错误: {str(e)}")
        raise SystemExit("程序终止")

def main():
    url_login = "http://10.99.99.32/srun_portal_pc?ac_id=1&theme=pro"
    url_success = "http://10.99.99.32/srun_portal_success?ac_id=1&theme=pro"
    username = "202311954"
    password = "041019wsr."

    # 指定 chromedriver 的路径
    chromedriver_path = r"D:\PythonProject\src\Automated-testing\chromedriver.exe"

    try:
        # 初始化 WebDriver
        driver = webdriver.Chrome(executable_path=chromedriver_path)
        driver.get(url_login)

        try:
            # 检查当前是否在已登录状态
            if driver.current_url.startswith(url_success):
                print("检测到用户已登录，执行注销流程")

                # 点击注销按钮
                logout_btn = WebDriverWait(driver, 10).until(
                    ec.element_to_be_clickable((By.ID, "logout"))
                )
                logout_btn.click()

                # 点击确认注销按钮（使用更稳定的选择器）
                confirm_btn = WebDriverWait(driver, 10).until(
                    ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'确认')]"))
                )
                confirm_btn.click()

                # 等待返回登录页面
                WebDriverWait(driver, 10).until(
                    ec.url_to_be(url_login)
                )
                print("注销成功")

            # 无论初始状态如何，最终都执行登录操作
            print("开始执行登录操作")
            login_user(driver, username, password)

        except (NoSuchElementException, TimeoutException) as e:
            print(f"操作过程中发生错误: {str(e)}")
        finally:
            # 适当延长观察时间后关闭
            driver.quit()

    except WebDriverException as e:
        print(f"初始化 WebDriver 时发生错误: {str(e)}")
        print("请检查 chromedriver 的路径是否正确，以及版本是否与 Chrome 浏览器匹配。")
        raise SystemExit("程序终止")

if __name__ == "__main__":
    main()