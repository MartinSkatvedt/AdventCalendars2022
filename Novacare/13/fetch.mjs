import fetch from 'node-fetch';

fetch("https://kodekalender.novacare.no/luke13", {
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "nb-NO,nb;q=0.9,no;q=0.8,nn;q=0.7,en-US;q=0.6,en;q=0.5",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "X-KODEKALENDER": "hemmelig",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": ".AspNetCore.Antiforgery.nixphHDAMN4=CfDJ8JHaeLyI_vpFmOxY9gEYxEjzBtTnw5fLU6MHoLE7DEHWddxlTsnP3h0r-77VelOXFoQMng6kgCSTOnKQ2iM0UXLMyRnmLERxBlaG77GBUcEB58JhrI6NrCGIlTNs8QBiKHnG7ehwK969PgAq1Ll6H-c; superkulkodekalenderbruker=cc1cf51a-5b3b-4654-9117-fdd6d399bac8; Luke7=1; Luke8=12",
    "Referer": "https://kodekalender.novacare.no/luke13",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": "answer=hemmelig&__RequestVerificationToken=CfDJ8JHaeLyI_vpFmOxY9gEYxEiMbsImvnP9rxW5aBDlIcVHv_ZnHSVfWQhci7qtYksMLc2q8h79gPrEAZP7hiJTvn0Y-J7bFlYeuUbXLUPQAZhRCc_4rasu3zX7DUFn2XtVCbcjAItdlxP6RVjt8vtLU-g",
  "method": "POST"
}).then((resp) => console.log(resp))

