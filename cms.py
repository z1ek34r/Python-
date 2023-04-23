import requests

cms_list = {
    "WordPress": ["wp-content", "wp-login.php", "wp-includes", "xmlrpc.php"],
    "Joomla": ["index.php?option=", "com_content", "com_users", "com_media"],
    "Drupal": ["sites/all", "modules/node"],
    "Magento": ["customer/account", "admin", "js/mage", "skin/frontend"],
    "OpenCart": ["index.php?route=", "admin/view"],
    "vBulletin": ["forumdisplay.php", "member.php?action=", "admincp"],
    "PrestaShop": ["modules/homepageadvertise", "admin"],
    "Shopify": ["cdn.shopify.com", "myshopify.com"],
    "phpBB": ["viewforum.php", "memberlist.php", "styles/prosilver"],
    "Django": ["django", "admin", "accounts/login", "media"],
}

def cms_detect(url):
    """
    探测URL所使用的CMS类型
    """
    for cms, keywords in cms_list.items():
        for keyword in keywords:
            res = requests.get(f"{url}/{keyword}")
            if res.status_code == 200 and cms in res.text:
                return cms
    return "Unknown"
if __name__ == '__main__':
    url = input('请输入要检测的 URL：')
    cms_type = cms_detect(url)
    print(f"{url} 使用的CMS类型为：{cms_type}")