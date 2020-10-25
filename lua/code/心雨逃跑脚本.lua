 if FX2 == nil then
  mm = gg.prompt({[1]="请输入密码"}, {[1]="0"}, {[1]="txet"})
  if mm[1] == "2325158781" then
    gg.toast("密码正确")
  else
    print(mm[1],"密码错误")
    os.exit()
  end
end
 function Main()                                                                                                    gg.toast("反馈群941636920")gg.toast("反馈群941636920")gg.toast("反馈群941636920")gg.toast("反馈群941636920")gg.toast("反馈群941636920")gg.toast("反馈群941636920")gg.toast("反馈群941636920")gg.toast("反馈群941636920")gg.toast("反馈群941636920")gg.toast("反馈群941636920")gg.toast("反馈群941636920")
  SN = gg.multiChoice({
  "🏆疾跑无限【大厅】🏆",
  "🏆疾跑10倍【大厅】🏆",
  "🏆隐身【大厅】🏆",
  "🏆秒开锁【游戏】🏆",
  "🏆待更新🏆",
  "🏆待更新🏆",
  "退出脚本"
 }, nil, "")
  if SN == nil then
  else
  if SN[1] == true then
   a()
  end
  if SN[2] == true then
   b()
  end
  if SN[3] == true then
   c()
  end
  if SN[4] == true then
   d()
  end
  if SN[5] == true then
   e()
  end
  if SN[6] == true then
   f()
  end
  if SN[7] == true then
   Exit()
  end
end
  XGCK = -1
end



function a()
gg.clearResults()
gg.setRanges(32)
gg.searchNumber("1000D;4.3;13D::", gg.TYPE_FLOAT, false, gg.SIGN_EQUAL, 0, -1)
gg.searchNumber("4.3", gg.TYPE_FLOAT, false, gg.SIGN_EQUAL, 0, -1)
gg.getResults(100)gg.editAll("999999", gg.TYPE_FLOAT)
gg.toast("南翼疾跑无限已开启")
gg.clearResults()
end



function b()
	 gg.clearResults()
	 gg.setRanges(32)
	 gg.searchNumber("6;0.3;0;0", gg.TYPE_FLOAT, false, gg.SIGN_EQUAL, 0, -1)
	 gg.searchNumber("0.3", gg.TYPE_FLOAT, false, gg.SIGN_EQUAL, 0, -1)
	 gg.getResults(100)
	 gg.editAll("3", gg.TYPE_FLOAT)
	 gg.toast("南翼10倍加速已开启")
	 gg.clearResults()
end



function c()
	 gg.clearResults()
	 gg.setRanges(32)
	 gg.searchNumber("103;400;500004", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1)
	 gg.searchNumber("103;400", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1)
	 gg.getResults(100)
	 gg.editAll("0", gg.TYPE_DWORD)
	 gg.toast("南翼隐身已开启")
	 gg.clearResults()
end



function d()
gg.clearResults()
gg.setRanges(32)
gg.searchNumber("1D;4;1D;1.2215521e-38;1D::", gg.TYPE_FLOAT, false, gg.SIGN_EQUAL, 0, -1)
gg.searchNumber("1.2215521e-38", gg.TYPE_FLOAT, false, gg.SIGN_EQUAL, 0, -1)
gg.getResults(100)
gg.editAll("66.878270031", gg.TYPE_FLOAT)
gg.toast("南翼秒开锁已开启")
gg.clearResults()
end



function e()
end



function f()
end



function Exit()
print("")
os.exit()
end
cs = ""



while true do
  if gg.isVisible(true) then
    XGCK = 1
    gg.setVisible(false)
  end
  gg.clearResults()
  if XGCK == 1 then
    Main()
  end
end









