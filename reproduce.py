from pathlib import Path
import subprocess,sys
root=Path(__file__).parent
for args in [['-m','unittest','discover','-p','test_model.py','-v'],['-m','unittest','discover','-s','asset_management','-v'],['run_analysis.py'],['asset_management/run.py'],['embassy_case/verify_case.py']]:
    subprocess.run([sys.executable,*args],cwd=root,check=True)
