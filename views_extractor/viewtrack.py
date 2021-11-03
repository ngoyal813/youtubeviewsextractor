api_key = "AIzaSyDZ2tTq4ha7T_Gdfz8NLbjjSIiOJi_4kxg"
from logging import error
from googleapiclient.discovery import build
from httplib2 import Response
from urllib.parse import urlparse, parse_qs

vidid = ["b66k4yh-Y6U","-u7vKPDkShE","AKtsbde2GxU","kLHZbABm8i8","r6d-DaLEo0Q","9llR53nKDyg","GCXKTfs4w1E","EDoA8nHFKhQ","TFm2QoxxUmo","ThbLv-FQ_Kk","IhEGOwglKB8","f8l72xAan_E","6aVusx0blJA","4-b5BkdoogQ","kcFESgfkl1k","OzGajIWoTn8","bMpzhafUom4","6UPKnzlsxBI","npJmWTmoZsg","hDG27jUJZTM","ni_RGlpBjd8","E4Iw957fZC8","wpVJ99AF_ug","VnKwh8ZCf1A","fISYBpCeEuU","hCmCbzOTc1A","iBozla1I9WI","hNMY6bnc-_U","GIbkAp6loX0","BQh0Fa_-sbs","FLwkColB4YM","Z0d2uDrOZ2M","8blkWdWwYsQ","dKvx1eckK5A","Co7FKpe99Fc","8blkWdWwYsQ","dKvx1eckK5A","Co7FKpe99Fc","t-eo49DYYUs","FAt4T65kSFA","v8OrwwJSWiw","wqoNbMECHP4","4pmM7e9uMNg","-EufZXdT9po","IVtmcKWP5pY","PI_vzE_S_Og","kLdPLYQ1DZk","NvRgLUtdrdM","Nhq8_hTPSQg","9amGfDmauN4","JLJJlJqleoY","5MiNGNiYeao","JBJjIwr2GqU","N8uh3x77yE4","20QXC2iSFmo","BgjcB5CQ_7c","zzjZIlEUuFc","AyKquchMnkw","ec3ex7cPLbA","ETU5lY5qaq4","lBPJNDCo_yo","hypFgj4krcM","C5UBlaxBWM8","vozEncXganc","CbLfJ_Sy9QA","zDUOVBnVai8","_7zG52IAYAE","XZKPTX8L8Z4","hmBLbdwfpyE","9B9dMS7IFY8","8filc1lVG_Q","PYVlFAW8BVg","BhjRSZP6RRY","f2JoXBiGRyU","0Kwtrc-lb34","axjLlYiyQhE","Y7uCL_zxLbw","a5TNE0oaTPM","b9KIx4Hio00","QYkjf85q5es","0Dc_Gaj_J5M","b9KIx4Hio00","CH5kruLqrNM","dat0Bhxujvk","z6Mm1QwY-UA","9rdaxxrT-FE","I2mj5Lts-X8","olaUroOyULg","PRDTIDFFeHk","zXmJoliNr_I","xWjOAX8OgGg","dTMypFeES0I","HIGMbuK0n4w","ZsC-mU1LY9U","6VN9ix7iyb0","nbbuS1acsf8","okGskTYHHmM","y2gY2nJhfZo","GXBsU4wmYhs","MUZdO_-o10Q","_aCaO-czxds","dMKzsEmI30A","9cSS0VcgDLU","Y5GiRIGrjGU","_3F8ZuVf6a4","9vSWJ6J99Ug","9cSS0VcgDLU","ggB318m1PAg","T-l4QrG532E","klVGmMmSURU","fJSwOVhhkTM","7dii_ki09gY","PTwe7WM-Lg8","g8SHloGjffk","AB22REW4Zus","xKYAwht0M1o","ezPqHNQ67SQ","YPW2_wJNUjk","vwkwUqj7wgs","X175o7L7Iek","X175o7L7Iek","crL4wOLqgb4","crL4wOLqgb4","cRRYFiLOi8o","4RIssHRKKhY","MQWo8vq0bLg","n7dCGc6M6AA","TURD4CxfRjI","QV0wHrXeEC4","UJ_PfLKN0n8","4wXG3W4T_gg","uVk-G4s5dEc","UJ_PfLKN0n8","tHaXm_Pi0fI","_D9VPNiwu4M","MkbeWaly_1s","lE8GADRyYqA","MkbeWaly_1s","nQCc1s5j9hE","ecXyLK4rpDw","9A0ROfRxIjA","pXqQoHDUcco","klXPTHIhbeY","aM_kXcSDkSc","DkPtxYodnBs","SdVdiyukkL8","z1QZbWZCwzQ","GzBbmM1DcsE","P7_wlX5Y39U","GzBbmM1DcsE","tiovnowYp9o","fkJu0I639aM","APSU8d86l9A","pDD3yhxz9Sc","jOorhovjL6c","R_73pgbYlK0","h2jJ_wm8uNc","dxF3oQvE1nA","jK4px22EpDQ","ArSdZD2qC9A","QLdRHV1en-M","USsL0m_CQTU","XhXG3POfEPA","jzo2lqGwn6g","8ToB5btK2G0","rLyzwTNk10I","_ZAtaDM_8EQ","QLdRHV1en-M","-GUYcJuk4GQ","PHduT2RJC40","XdgqDZsZzqw","KKhz4PyUeiU","q-3GS8l9cAo","XdgqDZsZzqw","vnlFnmuURac","-oTOvabC-Ao","mEzwLk3b9xA","aBYPNiJRp68","Qm6jNeSbRA0","Un8sgX0ZJ7c","RdDZtd1u5EA","J01NjDIojFY","evXiDuND6WY","qKCBnVcO9ZM","qHO1k2FgKvQ","qqxzsN37SnU","N6Z3sQpdLCI","GIgoq8BdMQI","QSmKSCRSygw","LvbqN49gYD4","ThenvS24F7I","GIgoq8BdMQI","AizocchYZHM","BQ4C2kFJwM8","ez3cQBp4Tiw","QNUeq_C5qAE","GfW_WfpGI2M","LKCIJctMhKI","18JzZ57S8XI","ez3cQBp4Tiw","0WwSJnTScu4","REG0tNFVvuI","GR8-A6vyyp8","noXItssCH20","4-nlHfI1o0c","c9ZI0JyVR-M","VcIGP0wP6qM","ZJtf5jXqeLA","Ai33hQ2A2M0","CgT2gN5jOi8","RnmNMm3WLsk","NCb7C8-pGgg","sd_GYxUaQzU","Z4EmXNCOqWA","zPriM6QUpUA","Y8VYZWFIRhI","Y7jA8DMtohk","ggNfv6wBm7o","VltdBjhSM4Y","jATlwqQ1KXk","qrpTcfzrzAg","ZABCegZOs2U","RJDcK2e46wA","eXp_XmlqORc","RJwpUJqxJQ8","0cSE2vOORnU","wHQ2p5eaBGA","SPuar2wLYig","tjmc7nJkSTg","Jd-VBQw__ow","5N-FoTdLP0Y","7aGLNaCc67M","mNscS5PcSgA","nzdMZBFXE6o","kfEcEfaKON0","n5KEVzYb-u0","eL8XYx0cptE","UG8el_mh-5A","I6ISbIinQ8Y","Yu9htXtd6Ag","p5Ky56jTw24","gqLVVuSogNI","4AYNXN2tSWs","944AHQdGWnk","L7EyoaZnusw","k6AYvmjjWjs","qjgplQT5WjQ","9zgUm49Qsok","5__qAzg66a0","uXjWY0EhLiM","5rrx2a9R5p0","2TfGrsB88Sg","CBe6LZMzC40","buwaFypMeSE","5CB51YLpWXM","BA2IRs-_G8U","pyDyhphsemk","tB24KvNTwS0","Oi50Gi0Ljj4","n-zDv794P1Q","7E0I9nZwT1M","VwE9qiML4U4","5b8vBKUnb8c","rh7SEoUGiUM","n6J_aIz-6UA","NqakwAGSUUA","SAAVGr04cd0","sADY00cwmHU","Q08kXgX0RW8","UULXEdpcQh0","DBF6TLkM3zA","YdVjbmaCGyc","K8p81PjluC0","OeZWhDvprSg","GDPhtWYrmqc","E7PoWoTnMYs","RedEsqsW_Gk","0w3vxS3e3D0","nIyxtRFFFEQ","_WsCSjiJlsM","s-Pv2WYBND8","6vHays0-bUA","u_ksQbjYpSI","Lt_rIK6hkCc","tOO2ebeYstY","isIYEsY9Fx4","TMZ7rwog4gk","hGfFsbrA8qQ","RnEMzQNPahM","jD9u8zJxhko","4Wn2GgqNgAg","62uoGNTmR8U","0YyI_MdcqG4","iM0asJBhlGs","agX-nzdYDz4","TMZ7rwog4gk","JakRF6-AHBE","mwa-CTETjEE","juWSoNNYQB0","RnEMzQNPahM","0vjZuc1dfzU","SVZiARQVVwQ","AYAhv_27XYo","XRwcBlpC-CM","Bv2-dJ7LC4k","08oUxPqLm9o","oSTLbn-lFRE","w1soHtI7xg8","dEy0vdlyiwY","R7a7_GpmEFg","vCSnIs8BnMY","Gpy6-bWGKIw","rdAMk9zcYMo","Q4KvyE2EaVw","0P3AEQpdOXo","Zii7jjZNj4U","Jfs_OT3VHCQ","C1vPQfxRfK4","HGfdjSaPnL4","lwig0VyoO0E","7ohD-xtHi8w","LWYGUXqiayU","JlHBvDYwDms","Ou5I1gHYha8","_1GKst3JWJo","uKMyLZHjR5I","FNSYUZOAHLY","VjR-YYAypug","y-Hp91EPx0A","mlTqVNvEKB8","e_H1jZq-fUw","rd8qEHr_WeQ","T05XX7uiwJA","YdeNgkFYHtc","ErVmHUJ_U2k","D2S99ONvrzU","hqxBycSp3_s","Fq2AdIxujqg","RYdY9rsARYY","JLN3RU-atC8","CIZrpQu6AqM","PPmR80RaB8g","y8ejws-CpL0","RyDxxy6Qmus","iEqEJkrppFo","ndoYTIEMz54","CgMu4oUBqVo","ulDlZ1W8Q_E","K8sPa5yPhq8","YcOJEa228Gs","qpZ_7vv_Wz0","XegADOqdLOc","99jKrpg_ZuY","HmHkmghIMec","wSHBSYd1a3A","9VphUmtPVVo","srVAGhSeYEg","imjrIymqUZQ","c0IUSmyunK8","Zpvw1jJai-c","F-1gi_dZMXI","DoQ3WXi8A1Y","oKAi36-znP8","THboPtrr8sg","I93X1wWoOmc","JK4Kc4_rUEE","JC5XTWBfOWU","gNldXry_4nQ","EXmoeVxhZqc","4hDJugvGQS8","gvov89nSz5Q","imTIWQgxNWk","L7f9YQ8dgv8","BIOGQ2ZQux0","c8uEb5pijRQ","aFeZHz7DMDY","r_J0D9wqxkU","r_IqpJ5KWbE","fJyZDt_lo6g","mLjPZQYotvg","AsMWTq1dzPc","17tJgprsDwI","L1-fivBqAtA","qPA9RLSNFYo","RrMXlkQ-BVs","IbMr_Moy9F4","Khq6l5ubI_8","9bbTkFrl9mI","hUH_yXr5otI","yH88Vic2IQ0","kA0F9QYFVCU","9nx_DximevU","jRqbAjNhlL0","grkBW6RrW4A","uvYc-7raxEE","cCBdWnmVamo","idL-u6nlJBk","RYj1SdD_Qng","lZwQ6wUxs9Q","GQIZDMKjMLo","FL-Y5usbzZg","MFdzMGQu2Fo","EGSRUpRcHoM","eLQcCxQLFLE","N3MAt0sVfog","X4Omh55JauI","1mzltQx0JSI","p9zZrkrTX6o","p0Z6Mr7Kxd8","CBTVag_d610","CBTVag_d610","8BXe4ejVJHo","7pwJr7qyzQs","QmiSegWiCgo","aHbVWN7-RbY","cHdklY0aWx0","y7c_c8P6o3I","Iptxr5JME5U","SvyoYEoj8UA","SvyoYEoj8UA","iX0CQp7xpbQ","gSh9Z3g2WwQ","gSh9Z3g2WwQ","KF7SP3TI_Q0","oI9vj7o7c_4","oY_0cuE8cvg","Ej17PTvUe2Q","G0VXQV_f6m4","V6GNWzphNbs","rc-bflILFjc","dvHCyqn2Y6Q","7tgLuSy0PPs","nftP01bd-J8","sao8VzPn_Y0","S-GDEWvesG4","wLyxDp6Jp0w","gLDgBDs97IE","K9rPZp1GSLA","cAaARlPkF9M","hgxfQyrsXxc","VOCNR9GjJs0","xm7dtHevHfA","yMo8rlPxxHo","E_jUfRj7zxE","iO0VUW6AWT8","5lVKd2Ztydg","IcDtNYWbXf0","Fij6Ii3XQcQ","OLH5EXfCulE","lKQfRtFh9Yg","i2OnN3jPJns","lqiIg_oA9Ms","iRNxx7L9Zic","xRTtUE93_-U","JItN558Xa0Y","UOvQiOcGYao","uM0eyC1VvKM","amIj8K0JtVg","O4Pp2o2OkI8","LFSQQygi9Og","pLmcWP6wQoY","7YErNH3gJ2c","jz5zxlELZ_4","uj92Smoh6jQ","fBeVK4uRQ48","3yDFl2jBGXE","x9QHkzPTeFo","rj2ziBlX-uM","ZWvLam2xPPI","Orz530VbsXo","V-Vg0O9WIkc","9RWSSJFi6OE","7RDpTXl9MiY","XRz-6sOgyz8","tLueWbyPDm0","EgU6GrzSExw","LjnxH0jer3U","xhfZgeAuNbI","crqSRz_7sJQ","-CNNvNWQfic","rLacB62qGaE","5Vni7F05bXQ","g8cNbME4m3c","R4_QY1ubioU","dvpmLm7zl0s","lEV7OINuIKc","HXErr7lUEPw","ZLry0bvlJD0","KHMji88rBpU","HP33BjkOmuk","tsir8Av_q-s","W61QqvFwJd0","VBrd12O0zJI","sp0gyJuan_0","i_RZoJippNU","6Jiy53SkS0s","6oDzWi8fH7I","oML_mcoAxq0","k-AX-6L6U3M","XI_H75DCOH8","XfLa69GB7Ng","1Uc1YGHJnKQ","KhvF3q84PGU","RViS6bgiTsc","-KIARojLNSc","MQYiG6DcRos","bPRjC53-zbg","aLEoY3ifgVM","SALVBl7n4Hg","AMwxpZ03reE","49CJvf7ojXU","-n0rlD-03VI","MH338qLKz6E","e0D7UU33o2o","P7tYV3INk8Q","Xg2HoBRKMMo","PkUiQ5KPVUU","m_HRPmRoT70","JZgzA8vokX4","Yc74eEtWqPM","prl1gh6fvUk","925NSvLsRGM","qKrBr_vaGmU","jwHfBJnTf5g","g0eiE4o1tBM","8iI3YkiJ8Cc","8UdzJ1mbyic"]
resultviews = []


def getvideodetails(videoid) :

    youtube = build('youtube','v3', developerKey=api_key)
    request = youtube.videos().list(part="statistics",id=videoid).execute()
    return request

for i in vidid :

    d = getvideodetails(i)
    if(d and d['items'] and d['items'][0] and d['items'][0]['statistics']) :

        views = d['items'][0]['statistics']['viewCount']
        resultviews.append(views)
    else :
        resultviews.append('0')

for i in resultviews :
    print(i)

