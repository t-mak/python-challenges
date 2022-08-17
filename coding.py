##14.4 CONCATENATING

##from PyPDF2 import PdfFileMerger
##from pathlib import Path
##
##pdf_merger = PdfFileMerger()
##
##print(Path.home())
##
##reports_dir = (
##    Path.home() /
##    "OneDrive" /
##    "Documents" /
##    "ch14-interact-with-pdf-files" /
##    "practice_files" /
##    "expense_reports"
##)
##
##
##print(reports_dir)
##
##expense_reports = list(reports_dir.glob("*.pdf"))
##expense_reports.sort()
##
##for path in expense_reports:
##    print(path.name)
##
##for path in expense_reports:
##    pdf_merger.append(str(path))
##
##with Path("expense_reports.pdf").open(mode="wb") as output_file:
##    pdf_merger.write(output_file)

##14.4 MERGING

##from PyPDF2 import PdfFileMerger
##from pathlib import Path
##
##pdf_merger = PdfFileMerger()
##
##reports_dir = (
##    Path.home() /
##    "OneDrive" /
##    "Documents" /
##    "ch14-interact-with-pdf-files" /
##    "practice_files" /
##    "quarterly_report"
##)
##
##report_path = reports_dir / "report.pdf"
##toc_path = reports_dir / "toc.pdf"
##
##pdf_merger.append(str(report_path))
##
##pdf_merger.merge(1, str(toc_path))
##
##with Path("full_report.pdf").open(mode="wb") as output_file:
##    pdf_merger.write(output_file)

##14.5 ROTATING PAGES
