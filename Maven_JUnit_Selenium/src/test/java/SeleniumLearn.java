/**
 * Класс для изучения Selenium Web Driver на Java
 */

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.net.URL;
import java.util.List;
import java.util.concurrent.TimeUnit;


public class SeleniumLearn {
    public ChromeDriver driver; //поле: информация о драйвере

    @Before
    public void setUp() {   //Метод выполняется до тестовых методов (подготовка)
        //Свойство для подключения драйвера
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\diodi\\Desktop\\Java\\chromedriver.exe");
        driver = new ChromeDriver();
    }

    @Test
    public void openSite() {
        driver.get("https://calculatori.ru/perevod-chisel.html");
        driver.manage().window().maximize();    //Откроет окно браузера на весь экран
        driver.manage().timeouts().implicitlyWait(15, TimeUnit.SECONDS);    //Ждать 15 сек

        WebElement inp = driver.findElement(By.id("Editbox1"));
        inp.sendKeys(Keys.BACK_SPACE);
        inp.sendKeys("10");

        //RadioButton пример работы: берем список всех позиций радиобатона, ищем по id
        List<WebElement> r_btn = driver.findElementsById("radio2");
        r_btn.get(4).click();   //из списка берем нужный и нажимаем на него

        WebElement btn = driver.findElementById("Button1");
        btn.click();

        //найти ответ и забрать из него текст с выводом на экран
        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
        WebElement answer = driver.findElementByXPath("//*[@id=\"table_calc\"]/table/tbody/tr[2]/td/b/font");
        System.out.println(answer.getText());
    }

    @Test
    public void testNewPage() {




    }


//    @After
//    public void close() {
//        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
//        driver.quit();  //close browser
//    }
}
